from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection URL
#helthsync.czu6w8q8setz.ap-southeast-1.rds.amazonaws.com
DATABASE_URL = "mysql+pymysql://admin:admin123@helthsync.czu6w8q8setz.ap-southeast-1.rds.amazonaws.com:3306/healthsync"

# SQLAlchemy engine and session setup
engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
