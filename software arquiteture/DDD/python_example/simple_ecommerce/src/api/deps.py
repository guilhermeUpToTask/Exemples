from typing import Annotated
from collections.abc import Generator
from fastapi import Depends, Query
from sqlmodel import Session

from src.application.catalog.dtos.product_dtos import ProductFilter
from src.infrastructure.db.database import get_engine
from src.application.catalog.uow.catalog_uow import CatalogUnitOfWork


def get_db() -> Generator[Session, None, None]:
    engine = get_engine()
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]


def get_catalog_uow(session: SessionDep) -> Generator[CatalogUnitOfWork, None, None]:
    with CatalogUnitOfWork(session) as uow:
        yield uow


CatalogUnitOfWorkDep = Annotated[CatalogUnitOfWork, Depends(get_catalog_uow)]

def get_product_filters(
    min_price: float | None = Query(None, ge=0),
    max_price: float | None = Query(None, ge=0),
    category: str | None= Query(None)
) -> ProductFilter:
    return ProductFilter(min_price=min_price, max_price=max_price, category=category)
ProductFiltersDep = Annotated[ProductFilter, Depends(get_product_filters)]