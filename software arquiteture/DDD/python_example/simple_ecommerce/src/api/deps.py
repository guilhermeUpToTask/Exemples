from typing import Annotated
from collections.abc import Generator
from fastapi import Depends, HTTPException, status
from sqlmodel import Session

from src.infrastructure.db.database import engine
from src.application.catalog.uow.catalog_uow import CatalogUnitOfWork


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]


def get_catalog_uow(session: SessionDep) -> Generator[CatalogUnitOfWork, None, None]:
    with CatalogUnitOfWork(session) as uow:
        yield uow


CatalogUnitOfWorkDep = Annotated[CatalogUnitOfWork, Depends(get_catalog_uow)]
