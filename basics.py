from sqlalchemy import Column, Integer, String, create_engine,text
from sqlalchemy.orm import DeclarativeBase, sessionmaker,Mapped, mapped_column

# 1. Model and Base Definiton
class Base(DeclarativeBase):
    pass

# Example User model
class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=True)

    def __repr__(self) -> str:
        return f"User(id={self.id}, name='{self.name}', email='{self.email}', age={self.age})"
    
# 2. Database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, echo=True)

# 3. Utilize 'sessionmaker' to create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Sessionlocal is now an instance of sessionmaker

# 4. Create tables in the database
Base.metadata.create_all(bind=engine)
print("...creating 'user' table.")

#5. Get a session instance from the factory and perform database operations
# Call Sessionlocal ()to get a session instance
with SessionLocal() as session:
    # A. Create a new user instance
    print("...adding a new user")
    new_user = User(name="Alice", email="aligce.gmail.com", age=30)
    # B. Add the new user to the session
    session.add(new_user)
    print("...added a new user:", new_user)
    # C. Commit the transaction to persist changes
    session.commit()
    print("...committed the transaction.")

print("...done.")