# 'postgresql://neondb_owner:npg_5GwKy9FfeMBt@ep-lucky-math-adevh1o2-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+psycopg2://neondb_owner:npg_5GwKy9FfeMBt@ep-lucky-math-adevh1o2-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for models
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
