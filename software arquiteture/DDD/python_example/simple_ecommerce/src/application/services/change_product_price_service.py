from src.domain.catalog.entities.product import Product
from src.domain.catalog.value_objects.price import Price
from src.domain.catalog.repositories.product_repository import ProductRepository


class ChangeProductPriceService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_id: str, new_price: float) -> Product:
        product = self.repository.get_by_id(product_id)
        if not product:
            raise ValueError("Product Not Found")

        product.price = Price(new_price)
        self.repository.update(product)

        return product
