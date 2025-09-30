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


def test_rename_product_success(rename_product_service, fake_repo):
    fake_repo.add(product1)
    assert (
        rename_product_service.execute("p1", "Light Blue Jeans").name.value
        == "Light Blue Jeans"
    )


def test_rename_product_wrong_name(rename_product_service, fake_repo):
    fake_repo.add(product1)
    assert rename_product_service.execute("p1", "Light Blue Jeans").name != "Wrong Name"


def test_rename_product_empty_name_raise(rename_product_service, fake_repo):
    fake_repo.add(product1)
    with pytest.raises(ValueError):
        rename_product_service.execute("p1", "")


def test_rename_product_not_found_raises(rename_product_service, fake_repo):
    fake_repo.add(product1)
    with pytest.raises(ValueError):
        rename_product_service.execute("p2", "Light Blue Jeans")
