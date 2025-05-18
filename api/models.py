import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



#Needed for querying the data from the database


class Price_Input(Base):
    __tablename__ = "price_information"

    id = Column(Integer, primary_key=True)
    ctype = Column(String)
    date = Column(DateTime)
    price = Column(Float)
    source_url = Column(String)
    scraped_at = Column(DateTime)
    
    
    
    
class Source_Input(Base):
    __tablename__ = "discovered_sources"

    id = Column(Integer, primary_key=True, index=True)
    source_site = Column(String, nullable=False)
    url = Column(String, nullable=False)
    is_pdf = Column(bool, default=True)
    keywords = Column(String)
    discovered_at = Column(DateTime, default=datetime.utcnow)