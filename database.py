# # database.py

# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "mysql+pymysql://root:piaus123@localhost/fastapi12"
# # Create SQLAlchemy engine
# engine = create_engine(DATABASE_URL)

# # Create a sessionmaker
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Base class for declarative models
# Base = declarative_base()
# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:piaus123@localhost/fastapi12"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

