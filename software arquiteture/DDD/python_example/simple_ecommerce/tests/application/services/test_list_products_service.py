from sqlalchemy.exc import IntegrityError
from typing import List
import pytest
from src.domain.catalog.value_objects.product_value_objects import (
    CategoryName,
    ProductName,
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
    category=CategoryName("t-shirts"),
    price=Price(200.0),
    description="A Yellow t-shirt",
)
product3 = Product(
    id=Product.next_id(),
    name=ProductName(" Red t-shirt"),
    category=CategoryName("t-shirts"),
    price=Price(200.0),
    description="A Red t-shirt",
)
product3_copy = Product(
    id=product3.id,
    name=ProductName(" Red t-shirt"),
    category=CategoryName("t-shirts"),
    price=Price(200.0),
    description="A Red t-shirt",
)

product4 = Product(
    id=Product.next_id(),
    name=ProductName(" Green t-shirt"),
    category=CategoryName("t-shirts"),
    price=Price(200.0),
    description="A Green t-shirt",
)


def test_list_all_products_success(list_products_service, catalog_uow):

    catalog_uow.products.add(product1)
    catalog_uow.products.add(product2)
    catalog_uow.products.add(product3)
    assert list_products_service.execute() == [product1, product2, product3]

    catalog_uow.products.add(product3_copy)
    with pytest.raises(IntegrityError):
        catalog_uow.commit()


def test_list_all_wrong_product_list(list_products_service, catalog_uow):
    catalog_uow.products.add(product1)
    catalog_uow.products.add(product2)
    catalog_uow.products.add(product3)
    assert list_products_service.execute() != [product1, product2, product3, product4]


def test_list_all_empty_products_success(list_products_service):
    assert len(list_products_service.execute()) == 0
    assert list_products_service.execute() == []


def test_list_all_products_dynamic_success(list_products_service, catalog_uow):
    catalog_uow.products.add(product1)
    catalog_uow.products.add(product2)
    assert list_products_service.execute() == [product1, product2]

    catalog_uow.products.add(product3)
    assert list_products_service.execute() == [product1, product2, product3]

    catalog_uow.products.delete(product2.id)
    assert list_products_service.execute() == [product1, product3]


def test_list_by_category_products_success(list_products_service, catalog_uow):
    correct_list: List = [product2, product3]
    catalog_uow.products.add(product1)
    catalog_uow.products.add(product2)
    catalog_uow.products.add(product3)
    assert list_products_service.execute("t-shirts") == correct_list


def test_list_by_category_products_invalid_category(list_products_service):
    with pytest.raises(ValueError):
        list_products_service.execute("Invalid Category Name")
