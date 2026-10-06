from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
from io import BytesIO

from config import ALLOWED_EXTENSIONS
from analyze import analyze_data
app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Form Analyzer API está funcionando!",
    }

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    # Verifica a extensão do arquivo
    extension = "." + file.filename.rsplit(".", 1)[-1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Formato não suportado. Use CSV ou XLSX"
        )

    # Lê o arquivo
    content = await file.read()

    try:
        if extension == ".csv":
            df = pd.read_csv(BytesIO(content))

        elif extension == ".xlsx":
            df = pd.read_excel(BytesIO(content))

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Não foi possível ler o arquivo."
        )

    # Envia o DataFrame para o analizador
    result = analyze_data(df)

    return result