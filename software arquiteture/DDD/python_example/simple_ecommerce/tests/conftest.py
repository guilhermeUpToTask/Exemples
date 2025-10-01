import pytest
from src.application.services.change_product_price_service import ChangeProductPriceService
from src.application.services.delete_product_service import DeleteProductService
from src.application.services.get_product_service import GetProductService
from src.application.services.rename_product_service import RenameProductService
from src.application.services.list_products_service import ListProductsService
from src.domain.catalog.entities.product import Product
from src.domain.catalog.value_objects.product_value_objects import CategoryName, ProductId
from src.domain.catalog.repositories.product_repository import ProductRepository
from src.application.services.register_product_service import RegisterProductService


class FakeProductRepository(ProductRepository):
    def __init__(self):
        self.products = {}

    def add(self, product: Product):
        self.products[product.id] = product

    def delete(self, product_id: ProductId):
        self.products.pop(product_id, None)

    def get_by_id(self, product_id: ProductId) -> Product | None:
        return self.products.get(product_id)

    def list_all(self):
        return list(self.products.values())

    def list_by_category(self, category: CategoryName):
        return [p for p in self.products.values() if p.category == category]

    def update(self, product: Product) -> Product:
        self.products[product.id] = product
        return product


@pytest.fixture
def fake_repo():
    return FakeProductRepository()


@pytest.fixture
def register_service(fake_repo):
    return RegisterProductService(repository=fake_repo)

@pytest.fixture
def list_products_service(fake_repo):
    return ListProductsService(fake_repo)

@pytest.fixture
def get_product_service(fake_repo):
    return GetProductService(fake_repo)

@pytest.fixture
def delete_product_service(fake_repo):
    return DeleteProductService(fake_repo)

@pytest.fixture
def change_product_price_service(fake_repo):
    return ChangeProductPriceService(fake_repo)

@pytest.fixture()
def rename_product_service(fake_repo):
    return RenameProductService(fake_repo)