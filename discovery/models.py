from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Source_Input(Base):
    __tablename__ = "discovered_sources"

    id = Column(Integer, primary_key=True, index=True)
    source_site = Column(String, nullable=False)
    url = Column(String, nullable=False)
    is_pdf = Column(bool, default=True)
    keywords = Column(String)
    discovered_at = Column(DateTime, default=datetime.utcnow)