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


class ClimateObservation(TimestampMixin):
    __tablename__ = "climate_observations"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    district_id: Mapped[int] = mapped_column(
        ForeignKey("districts.id"),
        nullable=False,
        index=True,
    )

    observation_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        index=True,
    )

    temperature_c: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    rainfall_mm: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    humidity_percent: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )
    
    aqi: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    heat_index_c: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    source: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    district = relationship(
    "District",
    back_populates="observations",
    )