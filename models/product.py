from config.database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey

class Product(Base):
    __tablename__ = "products"

    id= Column(Integer, primary_key= True, index= True)
    id_provider = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)