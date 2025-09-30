from dataclasses import dataclass

@dataclass(frozen=True)
class CategoryName:
    value: str

    def __post_init__(self):
        if self.value not in ["jeans", "shirts", "shoes", "sweaters"]:
            raise ValueError("Category name not in the Category List")
