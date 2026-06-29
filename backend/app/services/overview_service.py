from sqlalchemy import func
from sqlalchemy import select

from sqlalchemy.orm import Session

from app.models.district import District
from app.models.climate_health_index import (
    ClimateHealthIndex,
)
from app.models.risk_assessment import (
    RiskAssessment,
)


class OverviewService:

    @staticmethod
    def get_national_overview(
        db: Session,
    ):

        total_districts = db.scalar(
            select(func.count())
            .select_from(District)
        )

        districts_with_chi = db.scalar(
            select(
                func.count(
                    func.distinct(
                        ClimateHealthIndex.district_id
                    )
                )
            )
        )

        districts_with_risk = db.scalar(
            select(
                func.count(
                    func.distinct(
                        RiskAssessment.district_id
                    )
                )
            )
        )

        high_risk_districts = db.scalar(
            select(func.count())
            .select_from(RiskAssessment)
            .where(
                RiskAssessment.risk_level
                == "HIGH"
            )
        )

        severe_risk_districts = db.scalar(
            select(func.count())
            .select_from(RiskAssessment)
            .where(
                RiskAssessment.risk_level
                == "SEVERE"
            )
        )

        return {
            "total_districts": total_districts,
            "districts_with_chi": districts_with_chi,
            "districts_with_risk": districts_with_risk,
            "high_risk_districts": high_risk_districts,
            "severe_risk_districts": severe_risk_districts,
        }