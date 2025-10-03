from dataclasses import dataclass
from src.domain.shared.value_objects import GenericUUID


class ProductId(GenericUUID):
    pass


@dataclass(frozen=True)
class ProductName:
    value: str
    MAX_LENGTH = 100

    def __post_init__(self):
        name = self.value.strip()
        if not name:
            raise ValueError("Product name cannot be empty")
        if len(self.value) > self.MAX_LENGTH:
            raise ValueError(f"Product name cannot exceed {self.MAX_LENGTH} characters")
        object.__setattr__(self, "value", name)


@dataclass(frozen=True)
class CategoryName:
    value: str

    def __post_init__(self):
        if self.value not in ["jeans", "t-shirts", "shoes", "sweaters"]:
            raise ValueError("Category name not in the Category List")
