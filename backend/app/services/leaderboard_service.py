from sqlalchemy import select
from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.models.district import District
from app.models.risk_assessment import RiskAssessment


class LeaderboardService:

    @staticmethod
    def get_high_risk_districts(
        db: Session,
        limit: int = 10,
    ):

        latest_assessments = (
            select(
                RiskAssessment.district_id,
                RiskAssessment.risk_score,
                RiskAssessment.risk_level,
                RiskAssessment.risk_type,
                RiskAssessment.assessment_date,
            )
            .distinct(
                RiskAssessment.district_id
            )
            .order_by(
                RiskAssessment.district_id,
                desc(
                    RiskAssessment.assessment_date
                ),
            )
            .subquery()
        )

        results = db.execute(
            select(
                District.district_name,
                District.state_name,
                latest_assessments.c.risk_score,
                latest_assessments.c.risk_level,
                latest_assessments.c.risk_type,
            )
            .join(
                latest_assessments,
                District.id
                == latest_assessments.c.district_id,
            )
            .order_by(
                desc(
                    latest_assessments.c.risk_score
                )
            )
            .limit(limit)
        ).all()
        
    @staticmethod
    def get_districts_by_risk_type(
        db: Session,
        risk_type: str,
        limit: int = 10,
    ):

        latest_assessments = (
            select(
                RiskAssessment.district_id,
                RiskAssessment.risk_score,
                RiskAssessment.risk_level,
                RiskAssessment.risk_type,
                RiskAssessment.assessment_date,
            )
            .distinct(
                RiskAssessment.district_id
            )
            .order_by(
                RiskAssessment.district_id,
                desc(
                    RiskAssessment.assessment_date
                ),
            )
            .subquery()
        )

        results = db.execute(
            select(
                District.district_name,
                District.state_name,
                latest_assessments.c.risk_score,
                latest_assessments.c.risk_level,
                latest_assessments.c.risk_type,
            )
            .join(
                latest_assessments,
                District.id
                == latest_assessments.c.district_id,
            )
            .where(
                latest_assessments.c.risk_type
                == risk_type
            )
            .order_by(
                desc(
                    latest_assessments.c.risk_score
                )
            )
            .limit(limit)
        ).all()

        return results

        