from fastapi import FastAPI

app = FastAPI(
    title="La Liga Statistics API",
    description="Backend API for La Liga Statistics dashboard",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"status": "ok", "message": "La Liga API is running"}