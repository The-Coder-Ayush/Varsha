from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Construct DB URL using SQLAlchemy URL.create to handle special characters safely
DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    host=settings.POSTGRES_HOST,
    port=settings.POSTGRES_PORT,
    database=settings.POSTGRES_DB,
)

# Create the engine; pool_pre_ping avoids stale connections
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    hide_parameters=True  # Do not log query parameters (mask secrets).
)

# SessionLocal will be used to get DB sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
