from fastapi import FastAPI, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from db import get_db_session
from crawler import parse_pdf
import tempfile

app = FastAPI()

@app.post("/parse/")
async def parse_pdf_file(
    
    file: UploadFile = File(...),
    source_url: str = Form(...),
    db: Session = Depends(get_db_session)
):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    parse_pdf(tmp_path, source_url, db)
    return {"status": "success"}
