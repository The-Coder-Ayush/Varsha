from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.district import District


class SearchService:

    @staticmethod
    def search_districts(
        db: Session,
        query: str,
    ):
        statement = (
            select(District)
            .where(
                District.district_name.ilike(f"%{query}%")
            )
            .order_by(
                District.district_name.asc()
            )
        )

        result = db.execute(statement)

        return result.scalars().all()

    @staticmethod
    def search_states(
        db: Session,
        query: str,
    ):
        statement = (
            select(District.state_name)
            .distinct()
            .where(
                District.state_name.ilike(f"%{query}%")
            )
            .order_by(
                District.state_name.asc()
            )
        )

        result = db.execute(statement)

        return result.scalars().all()