from pydantic import BaseModel


class CHITrendPoint(BaseModel):
    date: str
    score: float


class RiskTrendPoint(BaseModel):
    date: str
    score: float
    level: str


class DistrictTrendResponse(BaseModel):
    district_id: int

    chi_history: list[CHITrendPoint]

    risk_history: list[RiskTrendPoint]