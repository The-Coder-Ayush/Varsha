from pydantic import BaseModel


class HighRiskDistrictResponse(
    BaseModel
):
    district_name: str
    state_name: str

    risk_score: float
    risk_level: str
    risk_type: str