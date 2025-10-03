from src.application.catalog.uow.abstract_unit_of_work import AbstractUnitOfWork
from src.domain.catalog.repositories.product_repository import ProductRepository
from src.infrastructure.repositories.product_repository import SQLModelProductRepository
from sqlmodel import Session


class CatalogUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session):
        self.session = session
        self.products: ProductRepository = SQLModelProductRepository(session)

    def __enter__(self) -> "CatalogUnitOfWork":
        return self

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
