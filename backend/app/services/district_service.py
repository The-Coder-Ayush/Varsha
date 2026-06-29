from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.district import District


class DistrictService:

    @staticmethod
    def get_district_by_id(
        db: Session,
        district_id: int,
    ):
        statement = (
            select(District)
            .where(District.id == district_id)
        )

        result = db.execute(statement)

        return result.scalar_one_or_none()