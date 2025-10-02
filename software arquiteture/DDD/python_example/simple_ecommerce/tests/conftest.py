import pytest
from sqlmodel import SQLModel, Session, create_engine
from src.domain.shared.value_objects import Price
from src.infrastructure.repositories.product_repository import (
    ProductDataMapper,
    SQLModelProductRepository,
)
from src.application.catalog.services.product_services import (
    ChangeProductPriceService,
    DeleteProductService,
    GetProductService,
    RenameProductService,
    ListProductsService,
    RegisterProductService,
)
from src.domain.catalog.entities.product import Product
from src.domain.catalog.value_objects.product_value_objects import (
    CategoryName,
    ProductId,
    ProductName,
)
from src.domain.catalog.repositories.product_repository import ProductRepository


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


# In-Memory SQLite
@pytest.fixture
def engine():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    yield engine
    engine.dispose()


@pytest.fixture
def session(engine):
    with Session(engine) as session:
        yield session


@pytest.fixture
def sqlmodel_product_repo(session):
    return SQLModelProductRepository(session, ProductDataMapper())


@pytest.fixture
def sample_product():
    return Product(
        id=Product.next_id(),
        name=ProductName("Blue Jeans"),
        price=Price(99.99),
        category=CategoryName("jeans"),
        description="A sample product for testing",
    )
