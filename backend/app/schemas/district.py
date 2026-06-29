from pydantic import BaseModel


class DistrictDetailsResponse(BaseModel):
    id: int
    district_code: str
    district_name: str
    state_name: str

    population: int | None
    area_km2: float | None

    latitude: float
    longitude: float