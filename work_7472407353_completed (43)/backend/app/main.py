from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routes import metrics, ai
from .auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Personal Server Monitor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(metrics.router, prefix="/metrics", tags=["metrics"])
app.include_router(ai.router, prefix="/ai", tags=["ai"])

@app.get("/health")
def health_check():
    return {"status": "online"}