from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.climate_health_index import (
    ClimateHealthIndex,
)
from app.models.risk_assessment import (
    RiskAssessment,
)


class TrendService:

    @staticmethod
    def get_district_trends(
        db: Session,
        district_id: int,
    ):

        chi_records = db.execute(
            select(ClimateHealthIndex)
            .where(
                ClimateHealthIndex.district_id
                == district_id
            )
            .order_by(
                ClimateHealthIndex.calculation_date
            )
        ).scalars().all()

        risk_records = db.execute(
            select(RiskAssessment)
            .where(
                RiskAssessment.district_id
                == district_id
            )
            .order_by(
                RiskAssessment.assessment_date
            )
        ).scalars().all()

        return {
            "chi_records": chi_records,
            "risk_records": risk_records,
        }