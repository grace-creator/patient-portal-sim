from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DB_USER = os.getenv("DB_USER", "patient_user")
DB_PASS = os.getenv("DB_PASS", "patient_pass")
DB_NAME = os.getenv("DB_NAME", "patient_db")
DB_HOST = os.getenv("DB_HOST", "db")  # service name in docker-compose

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
