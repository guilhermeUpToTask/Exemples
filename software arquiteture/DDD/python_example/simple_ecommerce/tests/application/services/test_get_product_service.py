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


def test_get_product_by_id(get_product_service, catalog_uow):
    catalog_uow.products.add(product1)
    catalog_uow.products.add(product2)
    catalog_uow.products.add(product3)
    assert get_product_service.execute(product2.id) == product2


def test_get_product_by_id_product_not_found_raises(get_product_service, catalog_uow):
    catalog_uow.products.add(product1)
    catalog_uow.products.add(product2)
    catalog_uow.products.add(product3)
    other_product_id = ProductId.next_id()
    with pytest.raises(ValueError):
        get_product_service.execute(other_product_id)
