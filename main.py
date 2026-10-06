from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
from io import BytesIO

from config import ALLOWED_EXTENSIONS
from analyzer import analyzer_data

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Form Analyzer API está funcionando!",
    }

@app.post("/analyze")
async def analyze(form: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }