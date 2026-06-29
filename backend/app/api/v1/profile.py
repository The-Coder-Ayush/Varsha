from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.district_profile import (
    DistrictProfileResponse,
)

from app.services.profile_service import (
    ProfileService,
)

router = APIRouter(
    prefix="/profiles",
    tags=["Profiles"],
)


@router.get(
    "/district/{district_id}",
    response_model=DistrictProfileResponse,
)
def get_profile(
    district_id: int,
    db: Session = Depends(get_db),
):

    profile = (
        ProfileService.get_district_profile(
            db=db,
            district_id=district_id,
        )
    )

    if profile is None:
        raise HTTPException(
            status_code=404,
            detail="District not found",
        )

    district = profile["district"]
    chi = profile["latest_chi"]
    risk = profile["latest_risk"]

    return DistrictProfileResponse(
        id=district.id,
        district_code=district.district_code,
        district_name=district.district_name,
        state_name=district.state_name,
        population=district.population,
        area_km2=district.area_km2,
        latitude=district.latitude,
        longitude=district.longitude,
        latest_chi_score=(
            chi.chi_score if chi else None
        ),
        latest_health_status=(
            chi.health_status if chi else None
        ),
        latest_risk_score=(
            risk.risk_score if risk else None
        ),
        latest_risk_level=(
            risk.risk_level if risk else None
        ),
        latest_risk_type=(
            risk.risk_type if risk else None
        ),
    )