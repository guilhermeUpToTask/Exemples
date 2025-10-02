import uuid
from dataclasses import dataclass
from typing import Any
from pydantic import GetCoreSchemaHandler


class GenericUUID(uuid.UUID):

    # generates id
    @classmethod
    def next_id(cls):
        return cls(int=uuid.uuid4().int)

    # makes this class be seen by pydantic as uuid
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ):
        return handler.generate_schema(uuid.UUID)


class ValueObject:
    """
    Base class for value objects
    """


# TODO: implement money value object here later
@dataclass(frozen=True)
class Money(ValueObject): ...
