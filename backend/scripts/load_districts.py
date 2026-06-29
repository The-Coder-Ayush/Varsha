from pathlib import Path

import pandas as pd

from app.database.session import SessionLocal
from app.models.district import District


CSV_PATH = Path("data/india_districts.csv")


def generate_district_code(
    state_name: str,
    district_name: str,
) -> str:

    state_part = "".join(
        word[0]
        for word in state_name.upper().split()
    )

    district_part = (
        district_name.upper()
        .replace(" ", "")
        .replace("&", "")
    )[:10]

    return f"{state_part}_{district_part}"


def safe_int(value):
    value = str(value).strip()

    if value in ["-", "", "nan", "NaN"]:
        return None

    try:
        return int(float(value))
    except Exception:
        return None


def safe_float(value):
    value = str(value).strip()

    if value in ["-", "", "nan", "NaN"]:
        return None

    try:
        return float(value)
    except Exception:
        return None


def main():
    df = pd.read_csv(CSV_PATH)

    db = SessionLocal()

    try:
        inserted = 0
        skipped = 0

        for _, row in df.iterrows():

            state_name = str(row["State"]).strip()
            district_name = str(row["District"]).strip()

            existing = (
                db.query(District)
                .filter(
                    District.district_name == district_name,
                    District.state_name == state_name,
                )
                .first()
            )

            if existing:
                skipped += 1
                continue

            population = safe_int(
                row["Population"]
            )

            area_km2 = safe_float(
                row["Area (in km^2)"]
            )

            latitude = safe_float(
                row["Latitude"]
            )

            longitude = safe_float(
                row["Longitude"]
            )

            if latitude is None or longitude is None:
                skipped += 1
                continue

            district = District(
                district_code=generate_district_code(
                    state_name,
                    district_name,
                ),
                district_name=district_name,
                state_name=state_name,
                population=population,
                area_km2=area_km2,
                latitude=latitude,
                longitude=longitude,
            )

            db.add(district)
            inserted += 1

        db.commit()

        print()
        print("=" * 50)
        print(f"Inserted: {inserted}")
        print(f"Skipped : {skipped}")
        print("=" * 50)

    except Exception as e:
        db.rollback()
        raise e

    finally:
        db.close()


if __name__ == "__main__":
    main()