from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.overview import (
    NationalOverviewResponse,
)

from app.services.overview_service import (
    OverviewService,
)

router = APIRouter(
    prefix="/overview",
    tags=["Overview"],
)


@router.get(
    "/national",
    response_model=NationalOverviewResponse,
)
def get_national_overview(
    db: Session = Depends(get_db),
):

    data = (
        OverviewService
        .get_national_overview(
            db=db
        )
    )

    return NationalOverviewResponse(
        **data
    )