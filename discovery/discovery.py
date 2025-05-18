import datetime
import requests
from bs4 import BeautifulSoup
import os
from sqlalchemy.orm import Session

from models import Source_Input
from db import get_db_session


KEYWORDS = ["coffee", "price"] 
EXTENSIONS = ".pdf"

BASE_URL = [
    "https://icocoffee.org/"
]


def related_pdf(href: str):
    return (href.lower().endswith(EXTENSIONS) and any(keyword in href.lower() for keyword in KEYWORDS))

def discover(start_url, db: Session):
    data = []
    
    print(f"Checking for pdfs in {start_url}")
    
    try:
        response = requests.get(start_url)
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a", href=True)
        
        for link in links:
            href = link["href"]
            full_url = os.path.join(start_url, href)
            
            if related_pdf(href):
                data.append(full_url)
                
                source = Source_Input(
                            source_site=start_url,
                            url=full_url,
                            is_pdf=True,
                            keywords=",".join([kw for kw in KEYWORDS if kw in href.lower()]),
                            discovered_at=datetime.utcnow()
                        )
                db.add(source)

        db.commit()
                
    except Exception as e:
        print(f"Error while checking {start_url}: {e}")
        db.rollback()

    db.close()
    return data