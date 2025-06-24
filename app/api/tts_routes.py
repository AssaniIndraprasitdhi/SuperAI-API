from fastapi import APIRouter
from pydantic import BaseModel
from app.services.tts_service import call_text2speech

router = APIRouter()

class TTSRequest(BaseModel):
    text: str
    speaker: str
    pace: int

@router.post("/tts")
async def tts(request: TTSRequest):
    return await call_text2speech(request.text, request.speaker, request.pace)
