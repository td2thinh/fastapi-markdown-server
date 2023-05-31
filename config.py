from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings

from model.note import Note
from model.tag import Tag
from decouple import config

MONGODB_URL = config('MONGODB_URL')

class Settings(BaseSettings):
    # database configurations
    DATABASE_URL: str = MONGODB_URL
    
    class Config:
        env_file = ".env"
        orm_mode = True


async def initiate_database():
    client = AsyncIOMotorClient(Settings().DATABASE_URL)
    try:
        client.admin.command("ping")
        print("Connected to MongoDB")
    except Exception as e:
        print("Unable to connect to MongoDB")
        print(e)
    await init_beanie(database=client.fastapi_server_markdown,
                      document_models=[Note, Tag])