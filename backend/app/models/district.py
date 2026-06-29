from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base_model import TimestampMixin

from sqlalchemy.orm import relationship


class District(TimestampMixin):
    __tablename__ = "districts"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    district_code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
    )

    district_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    state_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )
    
    
    population: Mapped[int | None] = mapped_column(
    Integer,
    nullable=True,
    )

    area_km2: Mapped[float | None] = mapped_column(
    Float,
    nullable=True,
    )

    latitude: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    longitude: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )
    
    observations = relationship(
    "ClimateObservation",
    back_populates="district",
    cascade="all, delete-orphan",
    )

    forecasts = relationship(
    "Forecast",
    back_populates="district",
    cascade="all, delete-orphan",
   )
    chi_records = relationship(
    "ClimateHealthIndex",
    back_populates="district",
    cascade="all, delete-orphan",
    )
    risk_assessments = relationship(
    "RiskAssessment",
    back_populates="district",
    cascade="all, delete-orphan",
    )