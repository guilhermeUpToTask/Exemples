from src.api.schemas.products import SimpleProductUpdate
from src.application.catalog.uow.catalog_uow import CatalogUnitOfWork
from src.domain.catalog.value_objects.product_value_objects import (
    CategoryName,
    ProductId,
    ProductName,
)
from src.domain.catalog.entities.product import Product
from src.domain.shared.value_objects import Price


# TODO: Commits should be done in unity of work for resuability of services
# TODO: Implement unity of work that will be in the place of repository when initialized the service
# TODO: Implment aggregation pattern after the basic of the project is ready to use


class RegisterProductService:
    def __init__(self, uow: CatalogUnitOfWork):
        self.uow = uow

    def execute(
        self, name: str, category: str, price: float, description: str = ""
    ) -> Product:
        product = Product(
            id=ProductId.next_id(),
            name=ProductName(name),
            category=CategoryName(category),
            price=Price(price),
            description=description,
        )

        self.uow.products.add(product)
        return product


class DeleteProductService:
    def __init__(self, uow: CatalogUnitOfWork):
        self.uow = uow

    def execute(self, product_id: ProductId):
        product = self.uow.products.get_by_id(product_id)
        if not product:
            raise ValueError("Product Not Found")
        self.uow.products.delete(product.id)


class GetProductService:
    def __init__(self, uow: CatalogUnitOfWork):
        self.uow = uow

    def execute(self, product_id: ProductId):
        product = self.uow.products.get_by_id(product_id)
        if not product:
            raise ValueError("Product Not Found")
        return product


class ListProductsService:
    def __init__(self, uow: CatalogUnitOfWork):
        self.uow = uow

    def execute(self, category: str | None = None):
        if category:
            cat = CategoryName(category)
            return self.uow.products.list_by_category(cat)
        return self.uow.products.list_all()


class ChangeProductPriceService:
    def __init__(self, uow: CatalogUnitOfWork):
        self.uow = uow

    def execute(self, product: Product, new_price: float):
        product.price = Price(new_price)
        self.uow.products.update(product)


class ChangeProductCategoryService:
    def __init__(self, uow: CatalogUnitOfWork):
        self.uow = uow

    def execute(self, product: Product, new_category: str):

        product.category = CategoryName(new_category)
        self.uow.products.update(product)

        return product


class UpdateProductSimpleFieldsService:
    def __init__(self, uow: CatalogUnitOfWork):
        self.uow = uow
        # Map field names to VO constructors if needed
        self.vo_mapping = {
            "name": ProductName,
        }

    def execute(self, product: Product, data: SimpleProductUpdate):

        for field, value in data.model_dump(exclude_unset=True).items():
            if value is None:
                raise ValueError(f"{field} cannot be None")
            converter = self.vo_mapping.get(field, lambda x: x)
            setattr(product, field, converter(value))

        self.uow.products.update(product)
        return product
