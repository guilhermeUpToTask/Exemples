from typing import List
import pytest
from src.domain.catalog.value_objects.product_value_objects import CategoryName, ProductName, ProductId
from src.domain.shared.value_objects import Price
from src.domain.catalog.entities.product import Product

product1 = Product(
    id=Product.next_id(),
    name=ProductName(" Blue Jeans"),
    category=CategoryName("jeans"),
    price=Price(200.0),
    description="A Blue Jeans",
)


def test_change_product_price_success(change_product_price_service, fake_repo):
    fake_repo.add(product1)
    assert change_product_price_service.execute(product1.id, 100.5).price.amount == 100.5


def test_change_product_invalid_price_raises(change_product_price_service, fake_repo):
    fake_repo.add(product1)
    with pytest.raises(ValueError):
        change_product_price_service.execute(product1.id, -20.5)


def test_change_product_not_found_raises(change_product_price_service, fake_repo):
    fake_repo.add(product1)
    other_product_id = ProductId.next_id()
    with pytest.raises(ValueError):
        change_product_price_service.execute(other_product_id, 100.5)
