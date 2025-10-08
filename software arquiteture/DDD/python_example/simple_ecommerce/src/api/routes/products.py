from fastapi import APIRouter, Depends, HTTPException, status
from uuid import UUID
from typing import List


from src.domain.catalog.value_objects.product_value_objects import ProductId
from src.application.catalog.services.product_services import (
    FindProductsWithFilters,
    GetProductService,
    RegisterProductService,
    DeleteProductService,
    ChangeProductPriceService,
    ChangeProductCategoryService,
    UpdateProductSimpleFieldsService,
)
from src.api.schemas.products import (
    ProductCreate,
    ProductRead,
    ProductUpdate,
)
from src.api.deps import CatalogUnitOfWorkDep, ProductFiltersDep

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductRead)
def create_product(data: ProductCreate, uow: CatalogUnitOfWorkDep):
    service = RegisterProductService(uow)
    product = service.execute(
        name=data.name,
        category=data.category,
        price=data.price,
        description=data.description,
    )
    return ProductRead.model_validate(product)


@router.get("/{product_id}", response_model=ProductRead)
def get_product(product_id: str, uow: CatalogUnitOfWorkDep):
    service = GetProductService(uow)
    try:
        product = service.execute(ProductId(product_id))
    except ValueError:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductRead.model_validate(product)


# TODO: implement pagination logic
@router.get("/", response_model=List[ProductRead])
def list_products(
    uow: CatalogUnitOfWorkDep,
    filters: ProductFiltersDep,
):
    service = FindProductsWithFilters(uow)
    products = service.execute(filters)
    
    return [ProductRead.model_validate(p) for p in products]


@router.delete("/product_id", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: str, uow: CatalogUnitOfWorkDep):
    service = DeleteProductService(uow)
    try:
        service.execute(ProductId(product_id))
    except ValueError:
        raise HTTPException(status_code=404, detail="Product not found")
    return


@router.patch("/{product_id}", response_model=ProductRead)
def update_product(product_id: str, data: ProductUpdate, uow: CatalogUnitOfWorkDep):
    product_id_vo = ProductId(product_id)

    product = GetProductService(uow).execute(product_id_vo)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    #TODO: Analizes the possible raised exceptions and map to correspondent statuscode
    UpdateProductSimpleFieldsService(uow).execute(
        product=product, new_name=data.name, new_description=data.description
    )

    if data.price is not None:
        ChangeProductPriceService(uow).execute(product, data.price)
    if data.category is not None:
        ChangeProductCategoryService(uow).execute(product, data.category)

    return ProductRead.model_validate(product)
