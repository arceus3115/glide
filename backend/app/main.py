"""FastAPI application entry point."""

from fastapi import FastAPI

from app.api.routes import health, trips

app = FastAPI(
    title="Glide",
    description="Go where you want. Efficiently, without headaches.",
    version="0.1.0",
)

app.include_router(health.router)
app.include_router(trips.router)

