from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.leaderboard import (
    HighRiskDistrictResponse,
)

from app.services.leaderboard_service import (
    LeaderboardService,
)

router = APIRouter(
    prefix="/leaderboard",
    tags=["Leaderboard"],
)


@router.get(
    "/high-risk-districts",
    response_model=list[
        HighRiskDistrictResponse
    ],
)
def get_high_risk_districts(
    db: Session = Depends(get_db),
):

    rows = (
        LeaderboardService
        .get_high_risk_districts(
            db=db
        )
    )

    return [
        HighRiskDistrictResponse(
            district_name=row.district_name,
            state_name=row.state_name,
            risk_score=row.risk_score,
            risk_level=row.risk_level,
            risk_type=row.risk_type,
        )
        for row in rows
    ]
    
@router.get(
    "/heatwave-districts",
    response_model=list[
        HighRiskDistrictResponse
    ],
)
def get_heatwave_districts(
    db: Session = Depends(get_db),
):

    rows = (
        LeaderboardService
        .get_districts_by_risk_type(
            db=db,
            risk_type="HEATWAVE",
        )
    )

    return [
        HighRiskDistrictResponse(
            district_name=row.district_name,
            state_name=row.state_name,
            risk_score=row.risk_score,
            risk_level=row.risk_level,
            risk_type=row.risk_type,
        )
        for row in rows
    ]


@router.get(
    "/air-quality-districts",
    response_model=list[
        HighRiskDistrictResponse
    ],
)
def get_air_quality_districts(
    db: Session = Depends(get_db),
):

    rows = (
        LeaderboardService
        .get_districts_by_risk_type(
            db=db,
            risk_type="AIR_QUALITY",
        )
    )

    return [
        HighRiskDistrictResponse(
            district_name=row.district_name,
            state_name=row.state_name,
            risk_score=row.risk_score,
            risk_level=row.risk_level,
            risk_type=row.risk_type,
        )
        for row in rows
    ]


@router.get(
    "/flood-risk-districts",
    response_model=list[
        HighRiskDistrictResponse
    ],
)
def get_flood_risk_districts(
    db: Session = Depends(get_db),
):

    rows = (
        LeaderboardService
        .get_districts_by_risk_type(
            db=db,
            risk_type="FLOOD",
        )
    )

    return [
        HighRiskDistrictResponse(
            district_name=row.district_name,
            state_name=row.state_name,
            risk_score=row.risk_score,
            risk_level=row.risk_level,
            risk_type=row.risk_type,
        )
        for row in rows
    ]