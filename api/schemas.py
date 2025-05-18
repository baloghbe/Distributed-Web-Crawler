from pydantic import BaseModel
from datetime import datetime


#For the GET requests from the database


class Discovered_Sources_Schema(BaseModel):
    id: int
    source_site: str
    url: str
    is_pdf: bool
    keywords: str
    discovered_at: datetime

    class Config:
        orm_mode = True



class Price_Data_Schema(BaseModel):
    id: int
    date: str
    price: str
    source_url: str
    scraped_at: datetime

    class Config:
        orm_mode = True