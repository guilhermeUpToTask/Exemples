from src.domain.catalog.errors import ProductNotFoundError
from src.infrastructure.db.mappers.product_filter_mapper import map_filters_to_spec
from src.application.catalog.dtos.product_dtos import ProductFilter
from src.application.catalog.uow.catalog_uow import CatalogUnitOfWork
from src.domain.catalog.value_objects.product_value_objects import (
    ProductId,
)
from src.domain.catalog.entities.product import Product


class RegisterProductService:
    """Application service to register a new product in the catalog."""

    def __init__(self, uow: CatalogUnitOfWork):
        self.uow = uow

    def execute(
        self, name: str, category: str, price: float, description: str
    ) -> Product:
        """
        Accepts raw input from the API layer.
        VO instantiation and validation happen inside the Product entity.
        """
        product = Product.create(
            name=name, category=category, price=price, description=description
        )
        self.uow.products.add(product)
        return product


class DeleteProductService:
    def __init__(self, uow: CatalogUnitOfWork):
        self.uow = uow

    def execute(self, product_id: ProductId):
        product = self.uow.products.get_by_id(product_id)
        if not product:
            # TODO: create product not found error for consistency and semantic.
            raise ProductNotFoundError("Product Not Found")
        self.uow.products.delete(product.id)

        return


class GetProductService:
    def __init__(self, uow: CatalogUnitOfWork):
        self.uow = uow

    def execute(self, product_id: ProductId):
        product = self.uow.products.get_by_id(product_id)
        if not product:
            raise ProductNotFoundError("Product Not Found")
        return product


class FindProductsWithFilters:
    def __init__(self, uow: CatalogUnitOfWork):
        self.uow = uow

    def execute(self, filters: ProductFilter):
        spec = map_filters_to_spec(filters)
        return self.uow.products.find_by_specification(spec)


class ChangeProductPriceService:
    def __init__(self, uow: CatalogUnitOfWork):
        self.uow = uow

    def execute(self, product: Product, new_price: float):
        product.change_price(new_price)
        self.uow.products.update(product)


class ChangeProductCategoryService:
    def __init__(self, uow: CatalogUnitOfWork):
        self.uow = uow

    def execute(self, product: Product, new_category: str):

        product.change_category(new_category)
        self.uow.products.update(product)

        return product


# TODO: VOs should be in the domain layer, this should call the method to update simples fields
class UpdateProductSimpleFieldsService:
    def __init__(self, uow: CatalogUnitOfWork):
        self.uow = uow
        # Map field names to VO constructors if needed

    # TODO:the data type should be a protocol
    def execute(
        self,
        product: Product,
        new_name: str | None = None,
        new_description: str | None = None,
    ):
        product.update_descriptive_info(name=new_name, description=new_description)
        self.uow.products.update(product)
        return product
