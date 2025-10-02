from typing import List
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
product2 = Product(
    id=Product.next_id(),
    name=ProductName(" Yellow t-shirt"),
    category=CategoryName("shirts"),
    price=Price(200.0),
    description="A Yellow t-shirt",
)
product3 = Product(
    id=Product.next_id(),
    name=ProductName(" Red t-shirt"),
    category=CategoryName("shirts"),
    price=Price(200.0),
    description="A Red t-shirt",
)
product3_copy = Product(
    id=product3.id,
    name=ProductName(" Red t-shirt"),
    category=CategoryName("shirts"),
    price=Price(200.0),
    description="A Red t-shirt",
)

product4 = Product(
    id=Product.next_id(),
    name=ProductName(" Green t-shirt"),
    category=CategoryName("shirts"),
    price=Price(200.0),
    description="A Green t-shirt",
)


def test_list_all_products_success(list_products_service, fake_repo):
    correct_list: List = [product1, product2, product3]

    fake_repo.add(product1)
    fake_repo.add(product2)
    fake_repo.add(product3)

    assert list_products_service.execute() == correct_list
    fake_repo.add(product3_copy)
    assert list_products_service.execute() == correct_list


def test_list_all_wrong_product_list(list_products_service, fake_repo):
    incorrect_list: List = [product1, product2, product3, product4]

    fake_repo.add(product1)
    fake_repo.add(product2)
    fake_repo.add(product3)

    assert list_products_service.execute() != incorrect_list


def test_list_all_empty_products_success(list_products_service):
    assert len(list_products_service.execute()) == 0
    assert list_products_service.execute() == []


def test_list_all_products_dynamic_success(list_products_service, fake_repo):
    correct_list: List = [product1, product2]
    fake_repo.add(product1)
    fake_repo.add(product2)
    assert list_products_service.execute() == correct_list
    correct_list = [product1, product2, product3]
    fake_repo.add(product3)
    assert list_products_service.execute() == correct_list
    correct_list = [product1, product3]
    fake_repo.delete(product2.id)
    assert list_products_service.execute() == correct_list


def test_list_by_category_products_success(list_products_service, fake_repo):
    correct_list: List = [product2, product3]
    fake_repo.add(product1)
    fake_repo.add(product2)
    fake_repo.add(product3)
    assert list_products_service.execute("shirts") == correct_list


def test_list_by_category_products_invalid_category(list_products_service):
    with pytest.raises(ValueError):
        list_products_service.execute("Invalid Category Name")
