# 🎹 Vaoja TTS API Proxy (FastAPI)

This is the backend API for Vaoja TTS Proxy, built with FastAPI.
It provides an abstraction layer to securely interact with [Vaoja API](https://vaoja-api.computing.kku.ac.th), allowing easy conversion of text (especially Isan/Thai) to speech.

---

## 📚 Table of Contents

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Folder Structure](#folder-structure)
4. [Setup & Installation](#setup--installation)

   * [.env Configuration](#env-configuration)
   * [Running the Application](#running-the-application)
5. [API Endpoints](#api-endpoints)
6. [Authentication](#authentication)
7. [Error Handling](#error-handling)
8. [Testing](#testing)
9. [License](#license)

---

## ✅ Features

* 🔁 Proxy integration with `/text2speech` from Vaoja API
* 📥 Accepts `text`, `speaker`, and `pace` as input
* 🔊 Returns `audio_url` and `qr_code` for the generated voice
* 🔒 Environment-based configuration using `.env`
* 🧱 Clean project structure: `api/`, `services/`, `core/`, `utils/`

---

## ⚙️ Tech Stack

| Layer         | Technology        |
| ------------- | ----------------- |
| Language      | Python 3.9+       |
| Framework     | FastAPI           |
| HTTP Client   | httpx (async)     |
| Config Loader | pydantic-settings |
| Server        | Uvicorn (ASGI)    |
| Docs          | Swagger / OpenAPI |

---

## 📂 Folder Structure

```
backend/
├── app/
│   ├── api/              # FastAPI routes
│   │   └── tts_routes.py
│   ├── core/             # Environment configuration
│   │   └── config.py
│   ├── services/         # Business logic
│   │   └── tts_service.py
│   ├── utils/            # Helper functions (e.g., HTTP client)
│   │   └── http_client.py
├── .env                  # Local environment variables
├── main.py               # Entry point
├── requirements.txt      # Python dependencies
```

---

## 🚀 Setup & Installation

### 1. Clone the Project

```bash
git clone https://github.com/your-username/Vaoja-TTS-Proxy.git
cd Vaoja-TTS-Proxy/backend
```

### 2. Create Virtual Environment and Install Dependencies

```bash
python -m venv .venv
source .venv/bin/activate           # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. .env Configuration

Create a `.env` file with the following:

```env
VAOJA_API_BASE=https://vaoja-api.computing.kku.ac.th
```

---

### 4. Running the Application

```bash
uvicorn main:app --reload
```

* Localhost: `http://127.0.0.1:8000`
* Swagger UI: `http://127.0.0.1:8000/docs`

---

## 📡 API Endpoints

### Text-to-Speech

| Method | Endpoint   | Description                       |
| ------ | ---------- | --------------------------------- |
| POST   | `/api/tts` | Converts text to speech via Vaoja |

#### Sample Request:

```json
{
  "text": "ว่าจั่งได๋นอ",
  "speaker": "mukda",
  "pace": 1
}
```

#### Sample Response:

```json
{
  "audio_url": "https://vaoja-api.computing.kku.ac.th/media/output.mp3",
  "qr_code": "https://vaoja-api.computing.kku.ac.th/media/output_qrcode.png"
}
```

---

## 🔐 Authentication

This proxy currently does **not require authentication**, but JWT or API Key support can be added as middleware if needed in production.

---

## ❌ Error Handling

* All errors are returned as structured JSON with appropriate status codes.
* FastAPI handles most validation (e.g., missing fields, wrong types).
* Additional logic can be added in a custom exception handler (e.g., for upstream API errors).

---

## 🧪 Testing

You can:

* Write tests using **pytest + httpx.AsyncClient**
* Mock upstream Vaoja API responses using `respx` or `pytest-httpx`
* Use `tests/` directory (recommended structure)

> Testing is not included yet in this boilerplate. PRs welcome!

---

## 📄 License

MIT License © 2025 [Assani Indraprasitdhi](https://github.com/AssaniIndraprasitdhi)
