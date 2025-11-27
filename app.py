# Import necessary components from our models file
# from models import User, create_database_tables, get_db_session
from model_postgresql import User, create_database_tables, get_db_session

def add_user_if_not_exists(email, name, fullname):
    # Use the 'get_db_session' function from models.py to create a new session instance
    with get_db_session() as session:
        print(f"--- Starting new database session/transaction ---")
        
        # Check if a user with this email already exists
        existing_user = session.query(User).filter_by(email=email).scalar()

        if existing_user:
            print(f"User with email {email} already exists. Skipping addition.")
        else:
            # Create and add the new user if they don't exist
            new_user = User(
                name=name,
                fullname=fullname,
                email=email
            )
            session.add(new_user)
            session.commit() # Commit the changes
            print(f"Added new user: {new_user.name}. Committed transaction.")


# Main application entry point
if __name__ == "__main__":
    # Ensure the database and tables are set up first
    create_database_tables()
    print("-" * 30)

    # Test adding two users (the second one will be skipped)
    add_user_if_not_exists(
        email="patrick@bikini.bottom",
        name="patrick",
        fullname="Patrick Star"
    )
    
    print("-" * 30)

    add_user_if_not_exists(
        email="patrick@bikini.bottom", # This email already exists
        name="patrick_duplicate",
        fullname="Patrick Star Duplicate"
    )
    
    print("\nApplication finished.")