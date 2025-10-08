from dataclasses import dataclass
from src.domain.shared.entities import Entity
from src.domain.shared.value_objects import Price
from src.domain.catalog.value_objects.product_value_objects import (
    ProductDescription,
    ProductId,
    ProductName,
    CategoryName,
)


# TODO: Later in the development this entity will became a aggregator and there where all the behavior will live
@dataclass(eq=False)
class Product(Entity[ProductId]):
    ID_CLASS = ProductId
    name: ProductName
    category: CategoryName
    price: Price
    description: ProductDescription

    # ----- Factory method for creation from primitives -----
    @classmethod
    def create(
        cls, name: str, category: str, price: float, description: str
    ) -> "Product":
        """
        Factory method to create a new Product from raw input.
        Performs VO instantiation and validation internally.
        """
        return cls(
            id=ProductId.next_id(),
            name=ProductName(name),
            category=CategoryName(category),
            price=Price(price),
            description=ProductDescription(description),
        )

    # ----- Behavior / domain methods -----
    def update_descriptive_info(
        self, name: str | None = None, description: str | None = None
    ):
        """
        Update product attributes that do not require complex business rules.
        Validation and normalization are enforced by the Value Objects.
        """
        if name is not None:
            self.name = ProductName(name)
        if description is not None:
            self.description = ProductDescription(description)

    def change_price(self, price: float):
        """
        Update product price.
        Future business rules or side-effects on price can be implemented here.
        """
        self.price = Price(price)

    def change_category(self, category: str):
        """
        Update product category.
        More complex behaviors related to category can be implemented here.
        """
        self.category = CategoryName(category)
