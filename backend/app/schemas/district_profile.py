from pydantic import BaseModel


class DistrictProfileResponse(
    BaseModel
):
    id: int
    district_code: str
    district_name: str
    state_name: str

    population: int | None
    area_km2: float | None

    latitude: float
    longitude: float

    latest_chi_score: float | None
    latest_health_status: str | None

    latest_risk_score: float | None
    latest_risk_level: str | None
    latest_risk_type: str | None