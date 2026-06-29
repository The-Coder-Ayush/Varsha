from fastapi import APIRouter

from app.schemas.climate_health_index import (
    CHICalculationRequest,
    CHICalculationResponse,
)

from app.services.chi_service import CHIService


router = APIRouter(
    prefix="/chi",
    tags=["CHI"],
)


@router.post(
    "/calculate",
    response_model=CHICalculationResponse,
)
def calculate_chi(
    request: CHICalculationRequest,
):

    chi_score = CHIService.calculate_chi(
        temperature_c=request.temperature_c,
        humidity_percent=request.humidity_percent,
        rainfall_mm=request.rainfall_mm,
        aqi=request.aqi,
        heat_index_c=request.heat_index_c,
    )

    return CHICalculationResponse(
    chi_score=chi_score,
    health_status=CHIService.get_health_status(
        chi_score
    ),
    top_contributors=CHIService.get_top_contributors(
        temperature_c=request.temperature_c,
        humidity_percent=request.humidity_percent,
        rainfall_mm=request.rainfall_mm,
        aqi=request.aqi,
        heat_index_c=request.heat_index_c,
    ),
)