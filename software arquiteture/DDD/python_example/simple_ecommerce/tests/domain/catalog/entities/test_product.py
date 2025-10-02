import pytest
from src.domain.catalog.entities.product import Product
from src.domain.shared.value_objects import Price
from src.domain.catalog.value_objects.product_value_objects import CategoryName, ProductName, ProductId

def test_create_product():
    product_id = ProductId.next_id()
    product = Product(
        id=product_id,
        name=ProductName("Blue Jeans"),
        category=CategoryName("jeans"),
        price=Price(200.0),
        description="A Blue Jeans",
    )

    assert product.id == product_id
    assert product.name.value == "Blue Jeans"
    assert product.category.value == "jeans"
    assert product.price.amount == 200.0
    assert product.description == "A Blue Jeans"


# Necessary to validate that's a id is what identify a entity, not its atributes
def test_product_equality_by_id():
    product_1 = Product(
        id=ProductId.next_id(),
        name=ProductName("Blue Jeans"),
        category=CategoryName("jeans"),
        price=Price(200.0),
    )
    product_2 = Product(
        id=product_1.id,#same id
        name=ProductName("Light Blue Jeans"),
        category=CategoryName("jeans"),
        price=Price(250.0),
    )

    assert product_1.id == product_2.id
