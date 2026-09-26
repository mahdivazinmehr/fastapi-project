from pydantic import BaseModel, Field, ConfigDict


class ProductCreate(BaseModel):
    name: str
    price: float = Field(gt=0)
    category: str


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    category: str

    model_config = ConfigDict(from_attributes=True)