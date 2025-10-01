import pytest
from src.domain.catalog.entities.product import Product
from src.domain.catalog.value_objects.price import Price
from src.domain.catalog.value_objects.product_value_objects import (
    CategoryName,
    ProductName,
    ProductId,
)
from src.domain.catalog.repositories.product_repository import ProductRepository


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
