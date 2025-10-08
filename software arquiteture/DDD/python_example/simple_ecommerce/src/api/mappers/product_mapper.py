from src.domain.catalog.entities.product import Product
from src.api.schemas.products import ProductRead


class ProductAPIMapper:
    @staticmethod
    def entity_to_read_model(entity: Product) -> ProductRead:
        return ProductRead(
            id=entity.id,
            name=entity.name.value,
            category=entity.category.value,
            price=entity.price.amount,
            description=entity.description.value,
        )
