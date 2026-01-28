from fastapi import FastAPI

app = FastAPI(
    title="Мій перший Pet-проєкт на FastAPI",
    description="Тестовий API для навчання",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {"message": "Вітаю! API працює 🚀", "docs": "/docs"}

@app.get("/health")
async def health_check():
    return {"status": "ok", "uptime": "running"}
