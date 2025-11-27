# models.py (PostgreSQL Version)

from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, Session

# 1. Setup the Declarative Base
class Base(DeclarativeBase):
    pass

# 2. Define the User Model
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[str]
    email: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r})"

# 3. Setup Database Connection Details using PostgreSQL URI
# Format: postgresql+psycopg2://user:password@host:port/database_name
DATABASE_URL = "postgresql+psycopg2://postgres:1234@localhost:5432/mydb" 
# NOTE: Replace 'postgres', 'secret', 'localhost:5432', and 'mydb' with your actual credentials

engine = create_engine(DATABASE_URL)

# 4. Configure a local session factory
SessionLocal = sessionmaker(bind=engine)

def create_database_tables():
    """Creates tables if they do not exist."""
    print("Attempting to connect to PostgreSQL and create tables...")
    Base.metadata.create_all(engine)
    print(f"Database tables ensured to exist in PostgreSQL instance.")

def get_db_session() -> Session:
    """Provides a session instance for use with 'with'."""
    return SessionLocal()