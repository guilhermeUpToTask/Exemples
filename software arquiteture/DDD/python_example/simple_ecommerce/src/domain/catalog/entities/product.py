from dataclasses import dataclass
from src.domain.catalog.value_objects.price import Price
from src.domain.catalog.value_objects.product_name import ProductName
from src.domain.catalog.value_objects.category_name import CategoryName

@dataclass
class Product:
    id: str
    name: ProductName
    category: CategoryName
    price: Price
    description: str = ""
