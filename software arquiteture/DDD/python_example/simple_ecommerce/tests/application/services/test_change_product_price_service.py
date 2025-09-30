from typing import List
import pytest
from src.domain.catalog.value_objects.category_name import CategoryName
from src.domain.catalog.value_objects.price import Price
from src.domain.catalog.value_objects.product_name import ProductName
from src.domain.catalog.entities.product import Product

product1 = Product(
    id="p1",
    name=ProductName(" Blue Jeans"),
    category=CategoryName("jeans"),
    price=Price(200.0),
    description="A Blue Jeans",
)


def test_change_product_price_success(change_product_price_service, fake_repo):
    fake_repo.add(product1)
    assert change_product_price_service.execute("p1", 100.5).price.amount == 100.5


def test_change_product_invalid_price_raises(change_product_price_service, fake_repo):
    fake_repo.add(product1)
    with pytest.raises(ValueError):
        change_product_price_service.execute("p1", -20.5)


def test_change_product_not_found_raises(change_product_price_service, fake_repo):
    fake_repo.add(product1)
    with pytest.raises(ValueError):
        change_product_price_service.execute("p2", 100.5)
