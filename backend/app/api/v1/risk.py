from fastapi import APIRouter

from app.schemas.climate_health_index import (
    CHICalculationRequest,
)

from app.schemas.risk_assessment import (
    RiskCalculationResponse,
)

from app.services.chi_service import CHIService
from app.services.risk_service import RiskService


router = APIRouter(
    prefix="/risk",
    tags=["Risk"],
)


@router.post(
    "/calculate",
    response_model=RiskCalculationResponse,
)
def calculate_risk(
    request: CHICalculationRequest,
):

    chi_score = CHIService.calculate_chi(
        temperature_c=request.temperature_c,
        humidity_percent=request.humidity_percent,
        rainfall_mm=request.rainfall_mm,
        aqi=request.aqi,
        heat_index_c=request.heat_index_c,
    )

    risk = RiskService.build_risk_assessment(
        chi_score=chi_score,
        temperature_c=request.temperature_c,
        rainfall_mm=request.rainfall_mm,
        aqi=request.aqi,
    )

    return RiskCalculationResponse(
        risk_score=risk["risk_score"],
        risk_level=risk["risk_level"],
        risk_type=risk["risk_type"],
    )