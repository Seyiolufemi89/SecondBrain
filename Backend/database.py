import sqlite3  # import sqlite3
from contextlib import closing # import contextlib because it is used to close the database connection after use
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Table #additional imports for SQLAlchemy
from sqlalchemy.orm import relationship, declarative_base # create a base class for declarative class definitions


DATABASE_URL = '"C:\\Users\\seyio\\Downloads\\sqlite-tools-win-x64-3540100\\mydata.db"'

def connect_db():
    return sqlite3.connect(DATABASE_URL)