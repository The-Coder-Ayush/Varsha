class RiskService:

    @staticmethod
    def get_risk_level(
        chi_score: float,
    ) -> str:

        if chi_score <= 25:
            return "LOW"

        if chi_score <= 50:
            return "MODERATE"

        if chi_score <= 75:
            return "HIGH"

        return "SEVERE"

    @staticmethod
    def get_risk_type(
        temperature_c: float,
        rainfall_mm: float,
        aqi: int | None,
    ) -> str:

        if temperature_c >= 40:
            return "HEATWAVE"

        if rainfall_mm >= 150:
            return "FLOOD"

        if aqi is not None and aqi >= 200:
            return "AIR_QUALITY"

        return "COMBINED"

    @classmethod
    def build_risk_assessment(
        cls,
        chi_score: float,
        temperature_c: float,
        rainfall_mm: float,
        aqi: int | None,
    ) -> dict:

        return {
            "risk_score": round(chi_score, 2),
            "risk_level": cls.get_risk_level(
                chi_score
            ),
            "risk_type": cls.get_risk_type(
                temperature_c,
                rainfall_mm,
                aqi,
            ),
        }