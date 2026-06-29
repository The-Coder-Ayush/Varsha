import sys
from pathlib import Path
from logging.config import fileConfig

from alembic import context

# Make app imports work
sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.database.base import Base
from app.database.session import engine
from app.models import *  # noqa: F401,F403


config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def include_object(
    object,
    name,
    type_,
    reflected,
    compare_to,
):
    """
    Ignore PostGIS system tables.
    Otherwise Alembic tries to manage them.
    """

    postgis_tables = {
        "spatial_ref_sys",
    }

    if type_ == "table" and name in postgis_tables:
        return False

    return True


def run_migrations_offline() -> None:
    """
    Offline migrations.
    We don't use this much in VARSHA,
    but keep it properly configured.
    """

    context.configure(
        url="",
        target_metadata=target_metadata,
        include_object=include_object,
        literal_binds=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """
    Online migrations using the same
    SQLAlchemy engine as FastAPI.
    """

    print("ALEMBIC USING SHARED ENGINE")

    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=include_object,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()