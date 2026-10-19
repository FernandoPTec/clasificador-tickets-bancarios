from pathlib import Path

import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


# Ruta principal del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
MODELO_DIR = BASE_DIR / "modelo"


# Cargar modelo y vectorizador
modelo = joblib.load(MODELO_DIR / "modelo_tickets.joblib")
tfidf = joblib.load(MODELO_DIR / "vectorizador_tfidf.joblib")


# Crear aplicación
app = FastAPI(
    title="Clasificador Inteligente de Tickets Bancarios",
    description="API para clasificación y priorización de tickets bancarios",
    version="1.0.0"
)


# Modelo de datos recibido por la API
class TicketEntrada(BaseModel):
    texto: str = Field(min_length=1)


# Áreas responsables
areas = {
    "fraude": "Prevención de Fraude",
    "tarjetas": "Atención de Tarjetas",
    "banca_digital": "Soporte Digital",
    "transferencias": "Operaciones Bancarias",
    "atencion_general": "Atención al Cliente"
}


# Reglas de prioridad
def obtener_prioridad(texto, categoria):

    texto = texto.lower()

    palabras_criticas = [
        "no reconozco",
        "robo",
        "robada",
        "fraude",
        "cargo no reconocido",
        "operación no reconocida"
    ]

    palabras_altas = [
        "bloqueada",
        "bloqueado",
        "no puedo entrar",
        "no puedo acceder",
        "rechazada",
        "rechazado"
    ]

    if categoria == "fraude" or any(p in texto for p in palabras_criticas):
        return "Crítica"

    elif any(p in texto for p in palabras_altas):
        return "Alta"

    elif categoria == "transferencias":
        return "Media"

    return "Baja"


@app.get("/")
def inicio():

    return {
        "mensaje": "API del Clasificador de Tickets Bancarios activa"
    }


@app.post("/predict")
def predecir_ticket(ticket: TicketEntrada):

    texto = ticket.texto.strip()

    if not texto:
        raise HTTPException(
            status_code=400,
            detail="El ticket no puede estar vacío"
        )

    # Convertir texto mediante TF-IDF
    texto_tfidf = tfidf.transform([texto])

    # Realizar predicción
    categoria = modelo.predict(texto_tfidf)[0]

    # Obtener prioridad
    prioridad = obtener_prioridad(texto, categoria)

    # Obtener área responsable
    area = areas.get(categoria, "Revisión manual")

    return {
        "ticket": texto,
        "categoria": categoria,
        "prioridad": prioridad,
        "area": area
    }
