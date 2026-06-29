from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.models.district import District
from app.models.climate_observation import (
    ClimateObservation,
)
from app.models.climate_health_index import (
    ClimateHealthIndex,
)
from app.models.risk_assessment import (
    RiskAssessment,
)
from app.services.forecast_service import ForecastService


class ClimateTwinService:

    @staticmethod
    def get_climate_twin(
        db: Session,
        district_id: int,
    ):

        district = db.get(
            District,
            district_id,
        )

        if district is None:
            return None

        latest_observation = db.execute(
            select(ClimateObservation)
            .where(
                ClimateObservation.district_id
                == district_id
            )
            .order_by(
                desc(
                    ClimateObservation.observation_date
                )
            )
            .limit(1)
        ).scalar_one_or_none()

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
        
        latest_forecast = (
    ForecastService.get_latest_forecast(
        db=db,
        district_id=district_id,
    )
)

        observation_count = db.scalar(
            select(func.count())
            .select_from(
                ClimateObservation
            )
            .where(
                ClimateObservation.district_id
                == district_id
            )
        )

        chi_count = db.scalar(
            select(func.count())
            .select_from(
                ClimateHealthIndex
            )
            .where(
                ClimateHealthIndex.district_id
                == district_id
            )
        )

        risk_count = db.scalar(
            select(func.count())
            .select_from(
                RiskAssessment
            )
            .where(
                RiskAssessment.district_id
                == district_id
            )
        )

        return {
            "district": district,
            "observation": latest_observation,
            "forecast": latest_forecast,
            "chi": latest_chi,
            "risk": latest_risk,
            "observation_count": observation_count,
            "chi_count": chi_count,
            "risk_count": risk_count,
            
        }