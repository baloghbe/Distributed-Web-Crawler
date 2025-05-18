from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, db

app = FastAPI()

def get_db():
    api_db = db.SessionLocal()
    try:
        yield api_db
    finally:
        api_db.close()




@app.get("/discovery", response_model=list[schemas.Discovered_Sources_Schema])
def get_sources(api_db: Session = Depends(get_db)):
    return api_db.query(models.Source_Input).all()




@app.get("/parse", response_model=list[schemas.Price_Data_Schema])
def get_prices(api_db: Session = Depends(get_db)):
    return api_db.query(models.Price_Input).all()