from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.search import (
    DistrictSuggestion,
    StateSuggestion,
)
from app.services.search_service import SearchService

router = APIRouter(
    prefix="/search",
    tags=["Search"],
)


@router.get(
    "/districts",
    response_model=list[DistrictSuggestion],
)
def search_districts(
    q: str,
    db: Session = Depends(get_db),
):
    districts = SearchService.search_districts(
        db=db,
        query=q,
    )

    return [
        DistrictSuggestion(
            district_name=d.district_name,
            state_name=d.state_name,
        )
        for d in districts
    ]


@router.get(
    "/states",
    response_model=list[StateSuggestion],
)
def search_states(
    q: str,
    db: Session = Depends(get_db),
):
    states = SearchService.search_states(
        db=db,
        query=q,
    )

    return [
        StateSuggestion(
            state_name=s,
        )
        for s in states
    ]