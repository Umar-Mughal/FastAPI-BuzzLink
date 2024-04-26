from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = (
#     "postgresql://<username>:<password>@<postgres_server or ip_address>/<database_name>"
# )
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:''@localhost:5432/fastapi-socialsite"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
