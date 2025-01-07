from app.database import SessionLocal, engine
from app.models import Base

# Create the database tables
Base.metadata.create_all(bind=engine)

# Test the connection
with SessionLocal() as db:
    print("Database connection successful!")
