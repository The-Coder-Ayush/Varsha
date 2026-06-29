class CHIService:

    @staticmethod
    def _temperature_stress(
        temperature_c: float,
    ) -> float:

        if temperature_c < 25:
            return 10

        if temperature_c < 35:
            return 40

        if temperature_c < 40:
            return 70

        return 100

    @staticmethod
    def _humidity_stress(
        humidity_percent: float,
    ) -> float:

        if humidity_percent < 40:
            return 20

        if humidity_percent < 70:
            return 50

        return 90

    @staticmethod
    def _aqi_stress(
        aqi: int | None,
    ) -> float:

        if aqi is None:
            return 0

        if aqi <= 50:
            return 10

        if aqi <= 100:
            return 30

        if aqi <= 200:
            return 70

        return 100

    @staticmethod
    def _rainfall_stress(
        rainfall_mm: float,
    ) -> float:

        if rainfall_mm < 50:
            return 20

        if rainfall_mm < 150:
            return 40

        return 90

    @staticmethod
    def _heat_index_stress(
        heat_index_c: float | None,
    ) -> float:

        if heat_index_c is None:
            return 0

        if heat_index_c < 30:
            return 20

        if heat_index_c < 40:
            return 50

        if heat_index_c < 50:
            return 80

        return 100

    @classmethod
    def calculate_chi(
        cls,
        temperature_c: float,
        humidity_percent: float,
        rainfall_mm: float,
        aqi: int | None,
        heat_index_c: float | None,
    ) -> float:

        chi_score = (
            cls._temperature_stress(temperature_c) * 0.30
            + cls._humidity_stress(humidity_percent) * 0.15
            + cls._aqi_stress(aqi) * 0.30
            + cls._rainfall_stress(rainfall_mm) * 0.10
            + cls._heat_index_stress(heat_index_c) * 0.15
        )

        return round(chi_score, 2)

    @staticmethod
    def get_health_status(
        chi_score: float,
    ) -> str:

        if chi_score <= 25:
            return "HEALTHY"

        if chi_score <= 50:
            return "MODERATE"

        if chi_score <= 75:
            return "HIGH_STRESS"

        return "SEVERE"
    
    @classmethod
    def get_top_contributors(
    cls,
    temperature_c: float,
    humidity_percent: float,
    rainfall_mm: float,
    aqi: int | None,
    heat_index_c: float | None,
   ):

      contributors = []

      if temperature_c >= 40:
        contributors.append("Extreme Temperature")

      if aqi is not None and aqi >= 200:
        contributors.append("Poor Air Quality")

      if humidity_percent >= 70:
        contributors.append("High Humidity")

      if heat_index_c is not None and heat_index_c >= 50:
        contributors.append("Dangerous Heat Index")

      if rainfall_mm >= 150:
        contributors.append("Heavy Rainfall")

      return contributors
    
    
    