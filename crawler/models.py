from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Price_Input(Base):
    __tablename__ = "price_information"

    id = Column(Integer, primary_key=True)
    ctype = Column(String)
    date = Column(DateTime)
    price = Column(Float)
    source_url = Column(String)
    scraped_at = Column(DateTime)