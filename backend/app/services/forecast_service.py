from sqlalchemy import desc
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.forecast import Forecast


class ForecastService:

    @staticmethod
    def get_latest_forecast(
        db: Session,
        district_id: int,
    ):

        forecast = db.execute(
            select(Forecast)
            .where(
                Forecast.district_id == district_id
            )
            .order_by(
                desc(Forecast.forecast_date)
            )
            .limit(1)
        ).scalar_one_or_none()

        return forecast