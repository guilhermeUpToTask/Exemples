import pytest
from src.domain.catalog.errors import ProductNotFoundError
from src.domain.catalog.value_objects.product_value_objects import (
    CategoryName,
    ProductDescription,
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
    description=ProductDescription("A Blue Jeans"),
)
product2 = Product(
    id=Product.next_id(),
    name=ProductName(" Yellow t-shirt"),
    category=CategoryName("t-shirts"),
    price=Price(200.0),
    description=ProductDescription("A Yellow t-shirt"),
)
product3 = Product(
    id=Product.next_id(),
    name=ProductName(" Red t-shirt"),
    category=CategoryName("t-shirts"),
    price=Price(200.0),
    description=ProductDescription("A Red t-shirt"),
)


def test_product_was_deleted(delete_product_service, catalog_uow):
    catalog_uow.products.add(product1)
    catalog_uow.products.add(product2)
    catalog_uow.products.add(product3)
    delete_product_service.execute(product2.id)

    assert catalog_uow.products.list_all() == [product1, product3]


def test_all_products_was_deleted(delete_product_service, catalog_uow):
    catalog_uow.products.add(product1)
    catalog_uow.products.add(product2)
    catalog_uow.products.add(product3)
    delete_product_service.execute(product1.id)
    delete_product_service.execute(product2.id)
    delete_product_service.execute(product3.id)

    assert len(catalog_uow.products.list_all()) == 0
    assert catalog_uow.products.list_all() == []


def test_product_not_found_for_deletion_raises(delete_product_service, catalog_uow):
    catalog_uow.products.add(product1)
    catalog_uow.products.add(product2)
    other_product_id = ProductId.next_id()
    with pytest.raises(ProductNotFoundError):
        delete_product_service.execute(other_product_id)
