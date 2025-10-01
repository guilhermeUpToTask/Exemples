from src.domain.catalog.value_objects.product_value_objects import CategoryName
from src.domain.catalog.repositories.product_repository import ProductRepository


class ListProductsService:
    def __init__(self, repository: ProductRepository) -> None:
        self.repository = repository

    def execute(self, category: str | None = None):
        if category:
            cat = CategoryName(category)
            return self.repository.list_by_category(cat)
        return self.repository.list_all()
