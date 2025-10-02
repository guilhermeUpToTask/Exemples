from typing import List
from uuid import UUID
import uuid
from sqlmodel import Field, SQLModel, Session, select
from src.domain.catalog.entities.product import Product
from src.domain.catalog.repositories.product_repository import ProductRepository
from src.domain.catalog.value_objects.product_value_objects import CategoryName, ProductId,ProductName
from src.domain.shared.value_objects import Price
from src.infrastructure.db.data_mapper import DataMapper



class ProductModel(SQLModel, table=True):
    __tablename__ = "products" #type: ignore
    id:UUID = Field(primary_key=True)
    name:str
    category:str
    price: float
    description: str = Field(default="No Description")


class ProductDataMapper(DataMapper[Product,ProductModel]):
    def model_to_entity(self, instance: ProductModel) -> Product:
        return Product(
            id=ProductId(str(instance.id)),
            name=ProductName(instance.name),
            price=Price(instance.price),
            category=CategoryName(instance.category),
            description=instance.description
        )
    
    def entity_to_model(self, entity: Product) -> ProductModel:
        return ProductModel(
            id=entity.id,
            name=entity.name.value,
            price=entity.price.amount,
            category=entity.category.value,
            description=entity.description
        )

class SQLModelProductRepository(ProductRepository):
    def __init__(self, session: Session, mapper:ProductDataMapper) -> None:
        self.session = session
        self.mapper = mapper

    def add(self, product: Product):
        product_model = self.mapper.entity_to_model(product)
        self.session.add(product_model)

    def delete(self, product_id):
        product_model = self.session.get(ProductModel, product_id)
        if product_model:
            self.session.delete(product_model)

    def get_by_id(self, product_id: ProductId) -> Product | None:
        product_model = self.session.get(ProductModel, product_id)
        if product_model:
            return self.mapper.model_to_entity(product_model)
        return None

    def list_all(self) -> List[Product]:
        product_models = self.session.exec(select(ProductModel)).all()
        return [self.mapper.model_to_entity(m) for m in product_models]

    def list_by_category(self, category: CategoryName) -> List[Product]:
        select_by_category_stmt = select(ProductModel).where(ProductModel.category == category.value)
        product_models = self.session.exec(select_by_category_stmt).all()
        return [self.mapper.model_to_entity(m) for m in product_models]

    def update(self, product: Product) -> Product:
        product_model = self.session.get(ProductModel, product.id)
        if not product_model:
            raise ValueError("Product not Found")
        
        product_model.sqlmodel_update(self.mapper.entity_to_model(product))
        self.session.add(product_model)
        
        return self.mapper.model_to_entity(product_model)

    def flush(self):
        self.session.flush()