
from contextlib import closing # import contextlib because it is used to close the database connection after use
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Table, create_engine #additional imports for SQLAlchemy
from sqlalchemy.orm import relationship, declarative_base, sessionmaker # create a base class for declarative class definitions


DATABASE_URL = "sqlite:///./database.db" # define the database URL for SQLite

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) # create an engine for the database connection

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # create a sessionmaker for creating sessions

def get_db(): # define a function to get a database session
    db = SessionLocal() # create a new session
    try:
        yield db # yield the session to be used in the context
    finally:
        db.close() # close the session after use