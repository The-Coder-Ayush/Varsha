from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.climate_twin import (
    ClimateTwinResponse,
    CurrentState,
    HealthState,
    RiskState,
    HistoricalSummary,
)

from app.services.climate_twin_service import (
    ClimateTwinService,
)

router = APIRouter(
    prefix="/climate-twin",
    tags=["Climate Twin"],
)


@router.get(
    "/district/{district_id}",
    response_model=ClimateTwinResponse,
)
def get_climate_twin(
    district_id: int,
    db: Session = Depends(get_db),
):

    twin = ClimateTwinService.get_climate_twin(
        db=db,
        district_id=district_id,
    )

    if twin is None:
        raise HTTPException(
            status_code=404,
            detail="District not found",
        )

    district = twin["district"]
    observation = twin["observation"]
    chi = twin["chi"]
    risk = twin["risk"]

    return ClimateTwinResponse(
        district_id=district.id,
        district_name=district.district_name,
        state_name=district.state_name,

        current_state=CurrentState(
            temperature_c=(
                observation.temperature_c
                if observation else None
            ),
            humidity_percent=(
                observation.humidity_percent
                if observation else None
            ),
            rainfall_mm=(
                observation.rainfall_mm
                if observation else None
            ),
            aqi=(
                observation.aqi
                if observation else None
            ),
            heat_index_c=(
                observation.heat_index_c
                if observation else None
            ),
        ),

        health_state=HealthState(
            chi_score=(
                chi.chi_score
                if chi else None
            ),
            health_status=(
                chi.health_status
                if chi else None
            ),
        ),

        risk_state=RiskState(
            risk_score=(
                risk.risk_score
                if risk else None
            ),
            risk_level=(
                risk.risk_level
                if risk else None
            ),
            risk_type=(
                risk.risk_type
                if risk else None
            ),
        ),

        historical_summary=HistoricalSummary(
            observation_count=twin[
                "observation_count"
            ],
            chi_count=twin[
                "chi_count"
            ],
            risk_count=twin[
                "risk_count"
            ],
        ),

        forecast_state=None,
    )