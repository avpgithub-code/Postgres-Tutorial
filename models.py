from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, Session

# 1. Setup the Declarative Base (Central registry for models)
class Base(DeclarativeBase):
    pass

# 2. Define the User Model (The 'users' table structure)
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[str]
    email: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r})"

# 3. Setup Database Connection Details
DATABASE_URL = "sqlite:///app_database.db"
engine = create_engine(DATABASE_URL)

# 4. Configure a local session factory
SessionLocal = sessionmaker(bind=engine)

# Function to ensure tables are created
def create_database_tables():
    """Creates tables if they do not exist."""
    Base.metadata.create_all(engine)
    print(f"Database tables ensured to exist in {DATABASE_URL}")

# Function to get a database session using the context manager pattern
def get_db_session() -> Session:
    """Provides a session instance for use with 'with'."""
    return SessionLocal()