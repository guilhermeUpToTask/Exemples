from dataclasses import dataclass
from src.domain.shared.entities import Entity
from src.domain.shared.value_objects import Price
from src.domain.catalog.value_objects.product_value_objects import (
    ProductId,
    ProductName,
    CategoryName,
)

#TODO: Later in the development this entity will became a aggregator and there where all the behavior will live
@dataclass
class Product(Entity[ProductId]):
    ID_CLASS = ProductId
    name: ProductName
    category: CategoryName
    price: Price
    description: str
