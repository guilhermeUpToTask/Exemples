from typing import List
import pytest
from src.domain.catalog.value_objects.product_value_objects import CategoryName, ProductName, ProductId
from src.domain.catalog.value_objects.price import Price
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

def test_product_was_deleted(delete_product_service, fake_repo):
    fake_repo.add(product1)
    fake_repo.add(product2)
    fake_repo.add(product3)
    delete_product_service.execute(product2.id)
    
    assert fake_repo.list_all() == [product1, product3]
    
    
def test_all_products_was_deleted(delete_product_service, fake_repo):
    fake_repo.add(product1)
    fake_repo.add(product2)
    fake_repo.add(product3)
    delete_product_service.execute(product1.id)
    delete_product_service.execute(product2.id)
    delete_product_service.execute(product3.id)
    
    assert len(fake_repo.list_all()) == 0
    assert fake_repo.list_all() == []

def test_product_not_found_for_deletion_raises(delete_product_service, fake_repo):
    fake_repo.add(product1)
    fake_repo.add(product2)
    other_product_id = ProductId.next_id()
    with pytest.raises(ValueError):
        delete_product_service.execute(other_product_id)
