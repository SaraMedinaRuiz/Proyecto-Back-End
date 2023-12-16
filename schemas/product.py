from typing import Optional
from pydantic import BaseModel, Field, validator

class Product(BaseModel):
    id: Optional[int] = None
    id_provider: int
    name: str = Field(default="Producto", min_length=5, max_length=30)
    description: str = Field(
        default="Descripcion del producto", min_length=10, max_length=300)
    category: str = Field(default="Aseo", min_length=3, max_length=15)
    price: int = Field(default=10000, ge=0)
    stock: int = Field(default=10)

class EditProduct(BaseModel):
    id: int
    price: int = Field(default=10000, ge=0)
    stock: int = Field(default=10)


# Configuracion de la documentacion
class Config:
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "id_provider": 1,
                    "name": "Producto",
                    "description": "Descripcion del producto",
                    "category": "Aseo",
                    "price": 1000,
                    "stock": 10
                }
            ]
        }
    }