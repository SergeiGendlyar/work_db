from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./crm_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

#engine = create_engine("mysql://iwatercrm:2bWcpBMau2bW3@95.213.183.180/iwater_test")

engine = create_engine("postgresql+psycopg2://iwatercrm:2bWcpBMau2bW33@95.213.183.180/iwater_test")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()