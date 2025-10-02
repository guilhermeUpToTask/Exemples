import pytest
from src.domain.catalog.value_objects.product_value_objects import (
    CategoryName,
    ProductName,
    ProductId,
)
from src.domain.shared.value_objects import Price
from src.domain.catalog.entities.product import Product

product1 = Product(
    id=Product.next_id(),
    name=ProductName(" Blue Jeans"),
    category=CategoryName("jeans"),
    price=Price(200.0),
    description="A Blue Jeans",
)


def test_rename_product_success(rename_product_service, fake_repo):
    fake_repo.add(product1)
    assert (
        rename_product_service.execute(product1.id, "Light Blue Jeans").name.value
        == "Light Blue Jeans"
    )


def test_rename_product_wrong_name(rename_product_service, fake_repo):
    fake_repo.add(product1)
    assert (
        rename_product_service.execute(product1.id, "Light Blue Jeans").name
        != "Wrong Name"
    )


def test_rename_product_empty_name_raise(rename_product_service, fake_repo):
    fake_repo.add(product1)
    with pytest.raises(ValueError):
        rename_product_service.execute(product1.id, "")


def test_rename_product_not_found_raises(rename_product_service, fake_repo):
    fake_repo.add(product1)
    other_product_id = ProductId.next_id()
    with pytest.raises(ValueError):
        rename_product_service.execute(other_product_id, "Light Blue Jeans")
