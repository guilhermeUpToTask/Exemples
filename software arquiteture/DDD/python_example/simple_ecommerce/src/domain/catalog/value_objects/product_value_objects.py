from dataclasses import dataclass
from src.domain.shared.value_objects import GenericUUID

class ProductId(GenericUUID):
    pass

@dataclass(frozen=True)
class ProductName:
    value:str
    
    def __post_init__(self):
        if not self.value.strip():
            raise ValueError("Product name cannot be empty")
@dataclass(frozen=True)
class CategoryName:
    value: str

    def __post_init__(self):
        if self.value not in ["jeans", "shirts", "shoes", "sweaters"]:
            raise ValueError("Category name not in the Category List")
