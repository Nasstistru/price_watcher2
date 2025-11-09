from sqlalchemy import create_engine, Column, String, Float, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class ProductDB(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    source = Column(String)
    rating = Column(Float)
    stock = Column(Boolean)

engine = create_engine("sqlite:///products.db")
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
