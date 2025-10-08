from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient
import pytest
from collections.abc import Generator
from sqlmodel import SQLModel, Session, StaticPool, create_engine
from typing import Annotated

from src.domain.shared.value_objects import Price
from src.domain.catalog.entities.product import Product
from src.domain.catalog.value_objects.product_value_objects import (
    CategoryName,
    ProductDescription,
    ProductName,
)

from src.infrastructure.repositories.product_repository import SQLModelProductRepository

from src.application.catalog.uow.catalog_uow import CatalogUnitOfWork
from src.application.catalog.services.product_services import (
    ChangeProductPriceService,
    ChangeProductCategoryService,
    UpdateProductSimpleFieldsService,
    DeleteProductService,
    GetProductService,
    FindProductsWithFilters,
    RegisterProductService,
)

from src.api.routes import products
from src.api.deps import get_catalog_uow, get_db


# Infrastructure Fixtures
@pytest.fixture
def engine():
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,  # 👈 This is the key
    )
    SQLModel.metadata.create_all(engine)
    yield engine
    engine.dispose()


@pytest.fixture
def session(engine):
    with Session(engine) as session:
        yield session


@pytest.fixture
def sqlmodel_product_repo(session):
    return SQLModelProductRepository(session)


@pytest.fixture
def catalog_uow(session):
    return CatalogUnitOfWork(session)


@pytest.fixture
def app(session):
    app = FastAPI()
    app.include_router(products.router)

    def _override_get_catalog_uow():
        with CatalogUnitOfWork(session) as uow:
            yield uow

    app.dependency_overrides[get_catalog_uow] = _override_get_catalog_uow

    return app


@pytest.fixture
def client(app):
    return TestClient(app)


# Samples
@pytest.fixture
def sample_product():
    return Product(
        id=Product.next_id(),
        name=ProductName("Blue Jeans"),
        price=Price(99.99),
        category=CategoryName("jeans"),
        description=ProductDescription("A sample product for testing"),
    )


# Services Fixture
@pytest.fixture
def register_service(catalog_uow):
    return RegisterProductService(catalog_uow)


@pytest.fixture
def find_products_with_filters(catalog_uow):
    return FindProductsWithFilters(catalog_uow)


@pytest.fixture
def get_product_service(catalog_uow):
    return GetProductService(catalog_uow)


@pytest.fixture
def delete_product_service(catalog_uow):
    return DeleteProductService(catalog_uow)


@pytest.fixture
def change_product_price_service(catalog_uow):
    return ChangeProductPriceService(catalog_uow)


@pytest.fixture()
def change_product_category_service(catalog_uow):
    return ChangeProductCategoryService(catalog_uow)


@pytest.fixture()
def update_product_simple_fields_services(catalog_uow):
    return UpdateProductSimpleFieldsService(catalog_uow)
