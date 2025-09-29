from typing import List
import pytest
from src.domain.catalog.entities.product import Product
from src.domain.catalog.value_objects.price import Price
from src.domain.catalog.value_objects.category_name import CategoryName
from src.domain.catalog.value_objects.product_name import ProductName
from src.domain.catalog.repositories.product_repository import ProductRepository
from src.application.services.register_product_service import RegisterProductService


# Fake Repository for tests
class FakeProductRepository(ProductRepository):
    def __init__(self):
        self.products = {}

    def add(self, product):
        self.products[product.id] = product

    def remove(self, product_id):
        self.products.pop(product_id, None)

    def get_by_id(self, product_id: str) -> Product | None:
        return self.products.get(product_id)

    def list_all(self) -> List[Product]:
        return list(self.products.values())


@pytest.fixture
def fake_repo():
    return FakeProductRepository()


@pytest.fixture
def register_service(fake_repo):
    return RegisterProductService(repository=fake_repo)


def test_register_product_success(register_service, fake_repo):
    product = register_service.execute(
        id="p1", name="Blue Jeans", category="jeans", price=200.0
    )
    # Should be in the repository
    assert fake_repo.get_by_id("p1") == product
    assert product.name.value == "Blue Jeans"
    assert product.price.amount == 200.0


def test_register_product_invalid_price_raises(register_service):
    with pytest.raises(ValueError):
        register_service.execute(
            id="p2", name="Blue Jeans", category="jeans", price=-100
        )
