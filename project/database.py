from motor.motor_asyncio import AsyncIOMotorClient
from sqlalchemy.ext.declarative import declarative_base
import os

# MONGODB_URL = "mongodb://localhost:27017"
MONGODB_URL = os.getenv("DATABASE_URL")
client = AsyncIOMotorClient(MONGODB_URL)
database = client["openaichat"]
Base = declarative_base()