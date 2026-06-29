from pydantic import BaseModel


class IntelligenceRequest(BaseModel):
    district_id: int

    temperature_c: float
    humidity_percent: float
    rainfall_mm: float

    aqi: int | None = None
    heat_index_c: float | None = None


class IntelligenceResponse(BaseModel):
    chi_score: float
    health_status: str

    risk_score: float
    risk_level: str
    risk_type: str

    top_contributors: list[str]