from sqlalchemy import inspect, text

from app.database.models import ai_tool, article, category, notification, saved_article, telegram_user, trending_topic, user_preference  # noqa: F401
from app.database.session.base import Base
from app.database.session.engine import engine


def _column_sql(column) -> str:
    compiled_type = column.type.compile(dialect=engine.dialect)
    statement = f"{column.name} {compiled_type}"
    default = getattr(column.default, "arg", None)
    if default is not None and not callable(default):
        if isinstance(default, bool):
            rendered = "1" if default else "0"
        elif isinstance(default, str):
            escaped_default = default.replace("'", "''")
            rendered = f"'{escaped_default}'"
        else:
            rendered = str(default)
        statement = f"{statement} DEFAULT {rendered}"
    return statement


def _reconcile_schema() -> None:
    inspector = inspect(engine)
    with engine.begin() as connection:
        for table in Base.metadata.sorted_tables:
            if not inspector.has_table(table.name):
                continue
            existing_columns = {column["name"] for column in inspector.get_columns(table.name)}
            for column in table.columns:
                if column.name in existing_columns:
                    continue
                connection.execute(text(f"ALTER TABLE {table.name} ADD COLUMN {_column_sql(column)}"))


def initialize_database() -> None:
    Base.metadata.create_all(bind=engine)
    _reconcile_schema()
