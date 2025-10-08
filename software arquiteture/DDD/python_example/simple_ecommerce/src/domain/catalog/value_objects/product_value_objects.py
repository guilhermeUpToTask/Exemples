from dataclasses import dataclass
from src.domain.shared.errors import InvalidValue
from src.domain.shared.value_objects import GenericUUID, DescriptiveString


class ProductId(GenericUUID):
    pass


class InvalidProductName(InvalidValue):
    pass


@dataclass(frozen=True)
class ProductName(DescriptiveString):
    MAX_LENGTH = 100
    EXCEPTION_CLASS = InvalidProductName
    FIELD_NAME = "Product name"


class InvalidDescription(InvalidValue):
    pass


@dataclass(frozen=True)
class ProductDescription(DescriptiveString):
    MAX_LENGTH = 300  # override default
    EXCEPTION_CLASS = InvalidDescription
    FIELD_NAME = "Product Description"


ALLOWED_CATEGORIES = {"jeans", "t-shirts", "shoes", "sweaters"}


class InvalidCategoryName(InvalidValue):
    pass


# TODO: category can become a entity as the project grows, be aware
@dataclass(frozen=True)
class CategoryName:
    value: str

    def __post_init__(self):
        if self.value not in ALLOWED_CATEGORIES:
            raise ValueError("Category name not in the Category List")
