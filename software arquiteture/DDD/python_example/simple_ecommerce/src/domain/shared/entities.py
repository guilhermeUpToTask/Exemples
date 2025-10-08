from dataclasses import dataclass, field
from typing import Any, ClassVar, Generic, Type, TypeVar, cast
from src.domain.shared.value_objects import GenericUUID

EntityId = TypeVar("EntityId", bound=GenericUUID)


@dataclass
class Entity(Generic[EntityId]):
    id: EntityId = field(compare=False)
    ID_CLASS: ClassVar[Type[GenericUUID]]

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Entity):
            return NotImplemented
        return self.id == other.id

    @classmethod
    def next_id(cls) -> EntityId:
        return cast(EntityId, cls.ID_CLASS.next_id())


class UserId(GenericUUID):
    pass


class OrderId(GenericUUID):
    pass


@dataclass
class User(Entity[UserId]):
    ID_CLASS = UserId
    name: str = ""


@dataclass
class Order(Entity[OrderId]):
    ID_CLASS = OrderId
    total: float = 0.0
