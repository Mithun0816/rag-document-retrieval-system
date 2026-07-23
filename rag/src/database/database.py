# database/database.py
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker
from config.config import config


class Database:
    def __init__(self):
        self.engine = self._create_engine()
        self.SessionLocal = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
        )

    def _create_engine(self):
        db_url = (
            f"postgresql+psycopg2://{config.db_username}:"
            f"{config.db_password}@"
            f"{config.db_host}:"
            f"{config.db_port}/"
            f"{config.db_name}"
        )
        return create_engine(db_url, future=True)

    # Use a **sync** generator dependency; only open/close the session here.
    def get_session(self):
        session = self.SessionLocal()
        try:
            yield session
        finally:
            session.close()

    def inspector(self, engine=None):
        # Allow optional engine param; default to self.engine
        return inspect(engine or self.engine)

    def test_connection(self) -> bool:
        """Test database connection (sync)."""
        try:
            with self.engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            return True
        except Exception:
            return False