from sqlalchemy import text

from app.database.session import engine


try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))

        print("SUCCESS")
        print(result.scalar())

except Exception as e:
    print("FAILED")
    print(type(e).__name__)
    print(e)