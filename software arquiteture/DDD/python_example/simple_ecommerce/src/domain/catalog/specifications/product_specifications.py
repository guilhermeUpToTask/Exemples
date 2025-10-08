from src.domain.shared.specifications import FieldSpecification, AndSpecification
from src.domain.catalog.value_objects.product_value_objects import CategoryName
from src.domain.shared.value_objects import Price
#TODO: later we will implement available system for products
def available_products() -> FieldSpecification:
    return FieldSpecification("is_available", "eq", True)

def is_in_category(category_name: str) -> FieldSpecification:
    cat = CategoryName(category_name)
    return FieldSpecification("category", "eq", cat.value)

def price_between(min_price: float, max_price: float) -> AndSpecification:
    min_price_vo = Price(min_price)
    max_price_vo = Price(max_price)
    return FieldSpecification("price", "gt", min_price_vo.amount).and_(
        FieldSpecification("price", "lt", max_price_vo.amount)
    )

