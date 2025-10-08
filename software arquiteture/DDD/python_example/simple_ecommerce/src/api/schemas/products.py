from fastapi import Query
from pydantic import BaseModel, Field
from uuid import UUID


class ProductCreate(BaseModel):
    name: str
    # TODO: create a single source of truth for category fields
    category: str
    price: float = Field(..., gt=0, description="Must be greater than 0")
    description: str = "No Description"


class ProductUpdate(BaseModel):
    name: str | None = None
    category: str | None = None
    price: float | None = Field(None, gt=0, description="Must be greater than 0")
    description: str | None = None



class ProductRead(BaseModel):
    id: UUID
    name: str
    category: str
    price: float
    description: str
    

