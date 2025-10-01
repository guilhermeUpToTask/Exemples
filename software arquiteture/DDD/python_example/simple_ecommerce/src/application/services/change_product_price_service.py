from src.domain.catalog.value_objects.product_value_objects import ProductId
from src.domain.catalog.entities.product import Product
from src.domain.catalog.value_objects.price import Price
from src.domain.catalog.repositories.product_repository import ProductRepository


# TODO: Commits should be done in unity of work for resuability of services
# TODO: Implement unity of work that will be in the place of repository when initialized the service
# TODO: Implment aggregation pattern after the basic of the project is ready to use
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
