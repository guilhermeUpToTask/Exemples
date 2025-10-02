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


@dataclass(frozen=True)
class Price(ValueObject):
    # atributes
    amount: float
    currency: str = "USD"

    # after init
    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Price cannot be negative")
