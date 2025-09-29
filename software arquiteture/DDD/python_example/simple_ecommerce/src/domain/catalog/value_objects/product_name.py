from dataclasses import dataclass

@dataclass(frozen=True)
class ProductName:
    value:str
    
    def __post_init__(self):
        if not self.value.strip():
            raise ValueError("Product name cannot be empty")