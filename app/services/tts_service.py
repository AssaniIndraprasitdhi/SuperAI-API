from app.utils.http_client import post_json
from app.core.config import settings

async def call_text2speech(text: str, speaker: str, pace: int):
    payload = {
        "text": text,
        "speaker": speaker,
        "pace": pace
    }
    url = f"{settings.vaoja_api_base}/text2speech"
    return await post_json(url, payload)
