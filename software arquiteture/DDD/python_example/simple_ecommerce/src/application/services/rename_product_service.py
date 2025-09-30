from src.domain.catalog.entities.product import Product
from src.domain.catalog.value_objects.product_name import ProductName
from src.domain.catalog.repositories.product_repository import ProductRepository


class UpdateProductPriceService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_id: str, new_name: str) -> Product:
        product = self.repository.get_by_id(product_id)
        if not product:
            raise ValueError("Product Not Found")

        product.name = ProductName(new_name)
        self.repository.update(product)

        return product
