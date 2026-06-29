from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.trend import (
    CHITrendPoint,
    RiskTrendPoint,
    DistrictTrendResponse,
)

from app.services.trend_service import (
    TrendService,
)

router = APIRouter(
    prefix="/trends",
    tags=["Trends"],
)


@router.get(
    "/district/{district_id}",
    response_model=DistrictTrendResponse,
)
def get_district_trends(
    district_id: int,
    db: Session = Depends(get_db),
):

    data = TrendService.get_district_trends(
        db=db,
        district_id=district_id,
    )

    return DistrictTrendResponse(
        district_id=district_id,

        chi_history=[
            CHITrendPoint(
                date=str(
                    record.calculation_date
                ),
                score=record.chi_score,
            )
            for record in data[
                "chi_records"
            ]
        ],

        risk_history=[
            RiskTrendPoint(
                date=str(
                    record.assessment_date
                ),
                score=record.risk_score,
                level=record.risk_level,
            )
            for record in data[
                "risk_records"
            ]
        ],
    )