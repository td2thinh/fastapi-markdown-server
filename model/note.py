from beanie import Document
from pydantic import BaseModel, Field
from .tag import Tag
from typing import Any, Optional, List


class Note(Document):
    title: str
    markdown: str
    tags: list[Tag] = []

    class Settings:
        collection = "notes"


class Response(BaseModel):
    message: dict
    data: Optional[Any] = None
    error: Optional[str] = None
