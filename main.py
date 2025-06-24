from fastapi import FastAPI
from app.api.tts_routes import router as tts_router

app = FastAPI(title="VaojaAPI Proxy")

app.include_router(tts_router, prefix="/api")
