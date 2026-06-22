import os
import time
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from pydub import AudioSegment

app = FastAPI()

# Permette al tuo frontend di comunicare con il backend Render senza blocchi di sicurezza (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In produzione metterai l'URL del tuo sito frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

APIFRAME_KEY = os.getenv("APIFRAME_API_KEY")

class RichiestaCanzone(BaseModel):
    occasione: str
    altra_occasione_testo: str = None
    dedicato_a: str
    relazione: str
    storia: str
    frasi_chiave: str
    genere: str
    email: EmailStr

@app.post("/api/crea-canzone")
async def crea_canzone(dati: RichiestaCanzone):
    try:
        # 1. Logica del testo e chiamata ad ApiFrame
        # (Usa le stesse funzioni viste nei messaggi precedenti)
        return {"status": "success", "message": "In elaborazione"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))