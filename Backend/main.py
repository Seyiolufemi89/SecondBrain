from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import engine
from models import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create the database tables if they don't exist
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)