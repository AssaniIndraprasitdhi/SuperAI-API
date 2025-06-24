# 🎙️ Vaoja TTS API Proxy (FastAPI)

ระบบ Proxy สำหรับใช้งาน Vaoja Text-to-Speech (TTS) API อย่างเป็นระบบ ด้วย FastAPI  
รองรับ `.env`, โครงสร้างแยกไฟล์ชัดเจน, และ API สำหรับแปลงข้อความอีสานเป็นเสียง

---

## 📦 คุณสมบัติ

- ✅ เชื่อมต่อกับ Vaoja API `/text2speech`
- ✅ รองรับพารามิเตอร์: `text`, `speaker`, `pace`
- ✅ คืนค่า `audio_url` และ `qr_code` จาก Vaoja API
- ✅ ใช้ FastAPI + httpx + pydantic-settings
- ✅ แยกไฟล์โครงสร้างชัดเจน: `api/`, `services/`, `utils/`, `core/`

---

## 🧱 โครงสร้างโปรเจกต์
backend/
├── app/
│ ├── api/ # FastAPI routes
│ │ └── tts_routes.py
│ ├── core/ # .env config
│ │ └── config.py
│ ├── services/ # Business logic
│ │ └── tts_service.py
│ ├── utils/ # HTTP client helper
│ │ └── http_client.py
├── .env
├── main.py # FastAPI entry point
├── requirements.txt


---

## ⚙️ วิธีติดตั้งและใช้งาน

### 1. Clone โปรเจกต์
```bash
git clone https://github.com/your-username/Vaoja-TTS-Proxy.git
cd Vaoja-TTS-Proxy/backend

2. สร้าง Virtual Environment และติดตั้ง dependency
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
3. สร้างไฟล์ .env
VAOJA_API_BASE=https://vaoja-api.computing.kku.ac.th
4. รันเซิร์ฟเวอร์ FastAPI
uvicorn main:app --reload
🚀 ตัวอย่างการใช้งาน API

POST /api/tts
Request Body:

{
  "text": "ว่าจั่งได๋นอ",
  "speaker": "mukda",
  "pace": 1
}
Response:

{
  "audio_url": "https://vaoja-api.computing.kku.ac.th/media/output.mp3",
  "qr_code": "https://vaoja-api.computing.kku.ac.th/media/output_qrcode.png"
}

📘 เทคโนโลยีที่ใช้

Tool	Description
FastAPI	Python Web Framework
httpx	Async HTTP client for Python
pydantic-settings	จัดการค่าจาก .env แบบปลอดภัย
Uvicorn	ASGI server สำหรับ FastAPI
🧑‍💻 ผู้พัฒนา

Assani Indraprasitdhi
💼 SuperAI ProjectM | 💡 Powered by Vaoja API
📍 Khon Kaen University

📄 License

MIT License © 2025 Assani Indraprasitdhi


---

คุณสามารถก็อปวางลงในไฟล์ `backend/README.md` ได้เลยครับ  
หากต้องการเวอร์ชันที่มี frontend รวมด้วยใน repo นี้ หรือเชื่อม API บนเว็บ GUI ก็บอกได้เลย ผมจะช่วยเขียน README เวอร์ชันเต็มให้อีกทีครับ ✅
