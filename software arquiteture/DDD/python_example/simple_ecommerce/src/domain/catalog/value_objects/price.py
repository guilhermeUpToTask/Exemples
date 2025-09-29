from dataclasses import dataclass

#imutable class, after instantiate cannot being modified, perfect for value objects as they are immutable aswell
@dataclass(frozen=True)
class Price:
    #atributes
    amount: float
    currency: str = "USD"
    
    #after init
    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Price cannot be negative")