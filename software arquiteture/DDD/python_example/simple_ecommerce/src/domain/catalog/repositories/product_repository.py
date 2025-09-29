#ABSTRACT BASE CLASS
#Used for creating interfaces from others classes
#this repository is where we define only the contracts, the implementations of it can be done for ay db in the infrastucture layer
#this possibility the domain layer to depends only the contracts
from abc import ABC, abstractmethod
from typing import List
from src.domain.catalog.entities.product import Product

class ProductRepository(ABC):
    @abstractmethod
    def add(self, product:Product) -> None:
        ...
    
    @abstractmethod
    def remove(self, product_id: str) -> None:
        ...
    
    @abstractmethod
    def get_by_id(self, product_id:str) -> Product | None:
        ...
    
    @abstractmethod
    def list_all(self) -> List[Product]:
        ...

