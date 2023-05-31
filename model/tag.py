from pydantic import BaseModel, Field
from typing import Optional, Any
from beanie import Document


class Tag(Document):
    name: str

    class Settings:
        collection = "notes"


class Response(BaseModel):
    message: dict
    data: Optional[Any] = None
    error: Optional[str] = None
