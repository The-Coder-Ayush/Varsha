from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.intelligence import (
    IntelligenceRequest,
    IntelligenceResponse,
)

from app.services.intelligence_service import (
    IntelligenceService,
)

router = APIRouter(
    prefix="/intelligence",
    tags=["Intelligence"],
)


@router.post(
    "/analyze",
    response_model=IntelligenceResponse,
)
def analyze(
    request: IntelligenceRequest,
    db: Session = Depends(get_db),
):

    result = IntelligenceService.analyze(
        db=db,
        district_id=request.district_id,
        temperature_c=request.temperature_c,
        humidity_percent=request.humidity_percent,
        rainfall_mm=request.rainfall_mm,
        aqi=request.aqi,
        heat_index_c=request.heat_index_c,
    )

    return IntelligenceResponse(**result)