from datetime import datetime
import pdfplumber
from sqlalchemy.orm import Session
from models import Price_Input
from db import get_db_session


def parse_pdf(path: str, url: str, db: Session):
    scraped_at = datetime.now()
    
    
    with pdfplumber.open(path) as pdf:
        
        for page in pdf.pages:
            table = page.extract_table()
            
            if table:
                for row in table[1:]:
                    date_str, c_type, price = row
                    date = datetime.strftime(date_str.strip(), "%Y-%m-%d")
                    entry = Price_Input(
                        id = None,
                        ctype=c_type.strip(),
                        price=float(price.strip()),
                        date=date,
                        source_url="", #Needs to be extracted from the previous table
                        scraped_at=scraped_at
                    )
                    db.add(entry)
                    
        db.commit()




            