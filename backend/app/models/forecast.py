from datetime import date

from sqlalchemy import Date
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_model import TimestampMixin


class Forecast(TimestampMixin):
    __tablename__ = "forecasts"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    district_id: Mapped[int] = mapped_column(
        ForeignKey("districts.id"),
        nullable=False,
        index=True,
    )

    forecast_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        index=True,
    )

    predicted_temperature_c: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    predicted_rainfall_mm: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    confidence_score: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    model_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    district = relationship(
        "District",
        back_populates="forecasts",
    )