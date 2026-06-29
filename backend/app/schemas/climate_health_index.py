from pydantic import BaseModel


class CHICalculationRequest(BaseModel):
    temperature_c: float
    humidity_percent: float
    rainfall_mm: float

    aqi: int | None = None
    heat_index_c: float | None = None


class CHICalculationResponse(BaseModel):
    chi_score: float
    health_status: str
    top_contributors: list[str]