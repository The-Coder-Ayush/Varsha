from pydantic import BaseModel


class NationalOverviewResponse(BaseModel):
    total_districts: int

    districts_with_chi: int

    districts_with_risk: int

    high_risk_districts: int

    severe_risk_districts: int