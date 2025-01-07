from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    medical_history = Column(Text, nullable=False)
