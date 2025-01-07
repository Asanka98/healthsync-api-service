from sqlalchemy import Column, Integer, String, Text, DateTime, Enum
from app.database import Base
import enum

class StatusEnum(str, enum.Enum):
    Pending = "Pending"
    Sent = "Sent"

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    notification_time = Column(DateTime, nullable=False)
    status = Column(Enum(StatusEnum), default="Pending")
