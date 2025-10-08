from dataclasses import dataclass


@dataclass
class ProductFilter:
    min_price: float | None = None
    max_price: float | None = None
    category: str | None = None
