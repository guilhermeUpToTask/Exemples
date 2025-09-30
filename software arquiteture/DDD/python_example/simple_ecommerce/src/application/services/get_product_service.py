from src.domain.catalog.repositories.product_repository import ProductRepository


class GetProductService:
    def __init__(self, repository: ProductRepository) -> None:
        self.repository = repository

    def execute(self, product_id: str):
        product = self.repository.get_by_id(product_id)
        if not product:
            raise ValueError("Product Not Found")
        return product
