import pytest
from src.domain.shared.value_objects import Price
from src.domain.catalog.value_objects.product_value_objects import (
    ProductName,
    CategoryName,
)


# TODO: Test Generic ID VO


# Price
def test_price_positive():
    price = Price(amount=100.0)
    assert price.amount == 100.0
    assert price.currency == "USD"


def test_price_negative_raises():
    with pytest.raises(ValueError):
        Price(amount=-10)


# Product Name
def test_product_name_valid():
    name = ProductName("Blue Jeans")
    assert name.value == "Blue Jeans"


def test_product_name_empty_raises():
    with pytest.raises(ValueError):
        ProductName("")


# Category Name
def test_category_name_valid():
    cat = CategoryName("jeans")
    assert cat.value == "jeans"


def test_category_name_invalid():
    with pytest.raises(ValueError):
        CategoryName("Invalid Name")
