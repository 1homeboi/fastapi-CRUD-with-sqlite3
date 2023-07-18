from pydantic import BaseModel, PositiveInt, Field


class ProductInput(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
    price: PositiveInt
