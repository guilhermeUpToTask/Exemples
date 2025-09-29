import pytest
from src.domain.catalog.entities.product import Product
from src.domain.catalog.value_objects.price import Price
from src.domain.catalog.value_objects.category_name import CategoryName
from src.domain.catalog.value_objects.product_name import ProductName
from src.domain.catalog.repositories.product_repository import ProductRepository


class RegisterProductService:
    """
    Aplication Service that register one product in the catalog
    """
    def __init__(self, repository: ProductRepository):
        self.repository = repository
        
    def execute(self, id: str, name: str, category:str, price:float, description:str = "")-> Product:
        product = Product(
            id=id,
            name=ProductName(name),
            category=CategoryName(category),
            price=Price(price),
            description=description
        )
        
        self.repository.add(product)
        
        return product