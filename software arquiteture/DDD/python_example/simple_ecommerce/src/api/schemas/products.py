from sqlmodel import Field, SQLModel
from uuid import UUID


class ProductCreate(SQLModel):
    name: str
    # TODO: create a single source of truth for category fields
    category: str
    price: float = Field(..., gt=0, description="Must be greater than 0")
    description: str = "No Description"


class ProductUpdate(SQLModel):
    name: str | None = None
    category: str | None = None
    price: float | None = Field(None, gt=0, description="Must be greater than 0")
    description: str | None

class SimpleProductUpdate(SQLModel):
    name: str | None = None
    description: str | None = None

class ProductRead(SQLModel):
    id: UUID
    name: str
    category: str
    price: float
    description: str

