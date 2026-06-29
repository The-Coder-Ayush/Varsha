from datetime import date

from sqlalchemy.orm import Session

from app.models.climate_health_index import ClimateHealthIndex
from app.models.risk_assessment import RiskAssessment

from app.services.chi_service import CHIService
from app.services.risk_service import RiskService


class IntelligenceService:

    @staticmethod
    def analyze(
        db: Session,
        district_id: int,
        temperature_c: float,
        humidity_percent: float,
        rainfall_mm: float,
        aqi: int | None,
        heat_index_c: float | None,
    ):

        chi_score = CHIService.calculate_chi(
            temperature_c=temperature_c,
            humidity_percent=humidity_percent,
            rainfall_mm=rainfall_mm,
            aqi=aqi,
            heat_index_c=heat_index_c,
        )

        health_status = CHIService.get_health_status(
            chi_score
        )

        contributors = CHIService.get_top_contributors(
            temperature_c=temperature_c,
            humidity_percent=humidity_percent,
            rainfall_mm=rainfall_mm,
            aqi=aqi,
            heat_index_c=heat_index_c,
        )

        risk = RiskService.build_risk_assessment(
            chi_score=chi_score,
            temperature_c=temperature_c,
            rainfall_mm=rainfall_mm,
            aqi=aqi,
        )

        chi_record = ClimateHealthIndex(
            district_id=district_id,
            calculation_date=date.today(),
            chi_score=chi_score,
            health_status=health_status,
            calculation_version="v1",
        )

        risk_record = RiskAssessment(
            district_id=district_id,
            assessment_date=date.today(),
            risk_score=risk["risk_score"],
            risk_level=risk["risk_level"],
            risk_type=risk["risk_type"],
        )

        db.add(chi_record)
        db.add(risk_record)

        db.commit()

        return {
            "chi_score": chi_score,
            "health_status": health_status,
            "risk_score": risk["risk_score"],
            "risk_level": risk["risk_level"],
            "risk_type": risk["risk_type"],
            "top_contributors": contributors,
        }