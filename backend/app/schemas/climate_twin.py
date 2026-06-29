from pydantic import BaseModel


class CurrentState(BaseModel):
    temperature_c: float | None
    humidity_percent: float | None
    rainfall_mm: float | None
    aqi: int | None
    heat_index_c: float | None


class HealthState(BaseModel):
    chi_score: float | None
    health_status: str | None


class RiskState(BaseModel):
    risk_score: float | None
    risk_level: str | None
    risk_type: str | None


class HistoricalSummary(BaseModel):
    observation_count: int
    chi_count: int
    risk_count: int


class ClimateTwinResponse(BaseModel):
    district_id: int
    district_name: str
    state_name: str

    current_state: CurrentState

    health_state: HealthState

    risk_state: RiskState

    historical_summary: HistoricalSummary

    forecast_state: dict | None = None