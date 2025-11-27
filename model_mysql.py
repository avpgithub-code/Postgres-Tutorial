# models.py (MySQL Version)

from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, Session

# 1. Setup the Declarative Base
class Base(DeclarativeBase):
    pass

# 2. Define the User Model
class User(Base):
    __tablename__ = "users"
    # Note: MySQL auto-increment PKs often work best starting at a high number 
    # if using very old versions, but this modern approach is fine for recent MySQL.
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(255), nullable=False) # Use sufficient length for MySQL VARCHAR

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r})"

# 3. Setup Database Connection Details using MySQL URI
# Format: mysql+mysqlconnector://user:password@host:port/database_name
DATABASE_URL = "mysql+mysqlconnector://root:1234@localhost:3306/mydb"
# NOTE: Replace 'root', 'secret', 'localhost:3306', and 'mydb' with your actual MySQL credentials

engine = create_engine(DATABASE_URL)

# 4. Configure a local session factory
SessionLocal = sessionmaker(bind=engine)

def create_database_tables():
    """Creates tables if they do not exist."""
    print("Attempting to connect to MySQL and create tables...")
    Base.metadata.create_all(engine)
    print(f"Database tables ensured to exist in MySQL instance.")

def get_db_session() -> Session:
    """Provides a session instance for use with 'with'."""
    return SessionLocal()