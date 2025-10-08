import pytest
from src.domain.catalog.value_objects.product_value_objects import (
    CategoryName,
    ProductDescription,
    ProductName,
)
from src.domain.shared.value_objects import Price
from src.domain.catalog.entities.product import Product
from src.application.catalog.dtos.product_dtos import ProductFilter

"""
Fixtures:
- catalog_uow: in-memory or transactional Unit of Work for catalog repo
- find_products_with_filters: application service to execute filtered queries
"""

product1 = Product(
    id=Product.next_id(),
    name=ProductName("Blue Jeans"),
    category=CategoryName("jeans"),
    price=Price(200.0),
    description=ProductDescription("A Blue Jeans"),
)
product2 = Product(
    id=Product.next_id(),
    name=ProductName("Yellow t-shirt"),
    category=CategoryName("t-shirts"),
    price=Price(250.0),
    description=ProductDescription("A Yellow t-shirt"),
)
product3 = Product(
    id=Product.next_id(),
    name=ProductName("Light Blue Jeans"),
    category=CategoryName("jeans"),
    price=Price(300.0),
    description=ProductDescription("A Light Blue Jeans"),
)

product4 = Product(
    id=Product.next_id(),
    name=ProductName("Green t-shirt"),
    category=CategoryName("t-shirts"),
    price=Price(350.0),
    description=ProductDescription("A Green t-shirt"),
)


@pytest.fixture
def sample_products():
    return [product1, product2, product3, product4]

def add_all(uow, products):
    for p in products:
        uow.products.add(p)

def test_return_all_products_when_no_filters(
    find_products_with_filters, catalog_uow, sample_products
):
    add_all(catalog_uow, sample_products)

    products = find_products_with_filters.execute(ProductFilter())
    assert set(products) == {product1, product2, product3, product4}


def test_filters_by_category(find_products_with_filters, catalog_uow, sample_products):
    add_all(catalog_uow, sample_products)

    t_shirt_products = find_products_with_filters.execute(
        ProductFilter(category="t-shirts")
    )
    assert set(t_shirt_products) == {product2, product4}


def test_filters_by_min_max_price(
    find_products_with_filters, catalog_uow, sample_products
):
    add_all(catalog_uow, sample_products)

    greater_than_products = find_products_with_filters.execute(
        ProductFilter(min_price=200.00)
    )
    assert set(greater_than_products) == {product2, product3, product4}

    smaller_than_products = find_products_with_filters.execute(
        ProductFilter(max_price=350.00)
    )
    assert set(smaller_than_products) == {product1, product2, product3}

    in_between_products = find_products_with_filters.execute(
        ProductFilter(min_price=200.00, max_price=350.00)
    )
    assert set(in_between_products) == {product2, product3}


def test_filters_combined_category_and_price_min_max(
    find_products_with_filters, catalog_uow, sample_products
):
    add_all(catalog_uow, sample_products)

    filtered_products = find_products_with_filters.execute(
        ProductFilter(category="t-shirts", min_price=200, max_price=350)
    )
    assert set(filtered_products) == {product2}


def test_no_matches_return_empty_list(
    find_products_with_filters, catalog_uow, sample_products
):
    add_all(catalog_uow, sample_products)

    empty_products = find_products_with_filters.execute(
        ProductFilter(category="does-not-exist")
    )
    assert empty_products == []
