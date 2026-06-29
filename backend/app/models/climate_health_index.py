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


class ClimateHealthIndex(TimestampMixin):
    __tablename__ = "climate_health_indices"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    district_id: Mapped[int] = mapped_column(
        ForeignKey("districts.id"),
        nullable=False,
        index=True,
    )

    calculation_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        index=True,
    )

    chi_score: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    health_status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    calculation_version: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="v1",
    )

    district = relationship(
        "District",
        back_populates="chi_records",
    )