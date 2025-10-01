from src.domain.catalog.value_objects.product_value_objects import (
    ProductId,
)
from src.domain.catalog.repositories.product_repository import ProductRepository

# Application Layer's Role: The Application Layer orchestrates the use cases of the system.
# tecnicals rules relies here on the aplication layer, if is a domain rule like if can be deleted then the rule relies on the domain layer


class DeleteProductService:

    def __init__(self, repository: ProductRepository) -> None:
        self.repository = repository

    def execute(self, product_id: ProductId):
        product = self.repository.get_by_id(product_id)
        if not product:
            raise ValueError("Product Not Founded")
        self.repository.delete(product.id)
