from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String(255), nullable=False)
    doctor_name = Column(String(255), nullable=False)
    appointment_time = Column(DateTime, nullable=False)
    reason = Column(String(255), nullable=True)
