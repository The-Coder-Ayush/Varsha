from fastapi import FastAPI
from sqlalchemy import text

from app.core.config import settings
from app.database.session import engine

from app.api.v1.search import router as search_router
from app.api.v1.districts import (
    router as districts_router,
)

from app.api.v1.chi import router as chi_router
from app.api.v1.risk import router as risk_router
from app.api.v1.intelligence import (
    router as intelligence_router,
)

from app.api.v1.profile import (
    router as profile_router,
)

from app.api.v1.leaderboard import (
    router as leaderboard_router,
)

from app.api.v1.trends import (
    router as trends_router,
)

from app.api.v1.climate_twin import (
    router as climate_twin_router,
)

from app.api.v1.overview import (
    router as overview_router,
)

app = FastAPI(
    title=settings.APP_NAME
)

app.include_router(
    search_router,
    prefix="/api/v1",
)

app.include_router(
    districts_router,
    prefix="/api/v1",
)

app.include_router(
    chi_router,
    prefix="/api/v1",
)

app.include_router(
    risk_router,
    prefix="/api/v1",
)

app.include_router(
    intelligence_router,
    prefix="/api/v1",
)

app.include_router(
    profile_router,
    prefix="/api/v1",
)

app.include_router(
    leaderboard_router,
    prefix="/api/v1",
)

app.include_router(
    trends_router,
    prefix="/api/v1",
)

app.include_router(
    climate_twin_router,
    prefix="/api/v1",
)

app.include_router(
    overview_router,
    prefix="/api/v1",
)


@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} Backend Running"
    }


@app.get("/health")
def health_check():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))

    return {
        "status": "healthy"
    }