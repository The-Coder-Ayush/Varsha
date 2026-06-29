from app.core.config import settings

print("USER:", settings.POSTGRES_USER)
print("HOST:", settings.POSTGRES_HOST)
print("PORT:", settings.POSTGRES_PORT)
print("DB:", settings.POSTGRES_DB)