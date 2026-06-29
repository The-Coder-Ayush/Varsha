from sqlalchemy import select
from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.models.district import District
from app.models.climate_health_index import (
    ClimateHealthIndex,
)
from app.models.risk_assessment import (
    RiskAssessment,
)


class ProfileService:

    @staticmethod
    def get_district_profile(
        db: Session,
        district_id: int,
    ):

        district = db.get(
            District,
            district_id,
        )

        if district is None:
            return None

        latest_chi = db.execute(
            select(ClimateHealthIndex)
            .where(
                ClimateHealthIndex.district_id
                == district_id
            )
            .order_by(
                desc(
                    ClimateHealthIndex.calculation_date
                )
            )
            .limit(1)
        ).scalar_one_or_none()

        latest_risk = db.execute(
            select(RiskAssessment)
            .where(
                RiskAssessment.district_id
                == district_id
            )
            .order_by(
                desc(
                    RiskAssessment.assessment_date
                )
            )
            .limit(1)
        ).scalar_one_or_none()

        return {
            "district": district,
            "latest_chi": latest_chi,
            "latest_risk": latest_risk,
        }