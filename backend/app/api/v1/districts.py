from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.district import (
    DistrictDetailsResponse,
)

from app.services.district_service import (
    DistrictService,
)

router = APIRouter(
    prefix="/districts",
    tags=["Districts"],
)


@router.get(
    "/{district_id}",
    response_model=DistrictDetailsResponse,
)
def get_district(
    district_id: int,
    db: Session = Depends(get_db),
):
    district = DistrictService.get_district_by_id(
        db=db,
        district_id=district_id,
    )

    if district is None:
        raise HTTPException(
            status_code=404,
            detail="District not found",
        )

    return DistrictDetailsResponse(
        id=district.id,
        district_code=district.district_code,
        district_name=district.district_name,
        state_name=district.state_name,
        population=district.population,
        area_km2=district.area_km2,
        latitude=district.latitude,
        longitude=district.longitude,
    )