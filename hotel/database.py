from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///hotel.db"

engine = create_engine(DATABASE_URL, echo = True)
SessionLocal = sessionmaker(bind = engine, autoflush = False)
Base = declarative_base()