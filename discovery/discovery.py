import requests
from bs4 import BeautifulSoup
import os

KEYWORDS = ["coffee", "price"] 
EXTENSIONS = ".pdf"

BASE_URL = [
    "https://icocoffee.org/"
]


def related_pdf(href: str):
    return (href.lower().endswith(EXTENSIONS) and any(keyword in href.lower() for keyword in KEYWORDS))

def discover(start_url):
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
                
    except Exception as e:
        print(f"Error while checking {start_url}: {e}")
        
    return data