from dataclasses import dataclass
from src.domain.shared.entities import Entity
from src.domain.catalog.value_objects.price import Price
from src.domain.catalog.value_objects.product_value_objects import ProductId, ProductName, CategoryName


@dataclass
class Product(Entity[ProductId]):
    ID_CLASS = ProductId
    name: ProductName
    category: CategoryName
    price: Price
    description: str = ""
