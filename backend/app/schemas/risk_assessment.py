from pydantic import BaseModel


class RiskCalculationResponse(BaseModel):
    risk_score: float
    risk_level: str
    risk_type: str