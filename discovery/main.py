from fastapi import FastAPI, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from db import get_db_session
from discovery import discover
import tempfile



app = FastAPI()

@app.post("/discover/")
async def discover_url(
    
    file: UploadFile = File(...),
    source_url: str = Form(...),
    db: Session = Depends(get_db_session)
):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    discover(source_url, db)
    return {"status": "success"}