from src.domain.catalog.value_objects.product_value_objects import (
    CategoryName,
    ProductId,
    ProductName,
)
from src.domain.catalog.entities.product import Product
from src.domain.shared.value_objects import Price
from src.domain.catalog.repositories.product_repository import ProductRepository


# TODO: Commits should be done in unity of work for resuability of services
# TODO: Implement unity of work that will be in the place of repository when initialized the service
# TODO: Implment aggregation pattern after the basic of the project is ready to use


class RegisterProductService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

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

        self.repository.add(product)

        return product


class DeleteProductService:

    def __init__(self, repository: ProductRepository) -> None:
        self.repository = repository

    def execute(self, product_id: ProductId):
        product = self.repository.get_by_id(product_id)
        if not product:
            raise ValueError("Product Not Founded")
        self.repository.delete(product.id)


class GetProductService:
    def __init__(self, repository: ProductRepository) -> None:
        self.repository = repository

    def execute(self, product_id: ProductId):
        product = self.repository.get_by_id(product_id)
        if not product:
            raise ValueError("Product Not Found")
        return product


class ListProductsService:
    def __init__(self, repository: ProductRepository) -> None:
        self.repository = repository

    def execute(self, category: str | None = None):
        if category:
            cat = CategoryName(category)
            return self.repository.list_by_category(cat)
        return self.repository.list_all()


class ChangeProductPriceService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_id: ProductId, new_price: float) -> Product:
        product = self.repository.get_by_id(product_id)
        if not product:
            raise ValueError("Product Not Found")

        product.price = Price(new_price)
        self.repository.update(product)

        return product


class RenameProductService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_id: ProductId, new_name: str) -> Product:
        product = self.repository.get_by_id(product_id)

        if not product:
            raise ValueError("Product Not Found")

        product.name = ProductName(new_name)
        self.repository.update(product)

        return product
