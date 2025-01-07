from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional  # Use Optional instead of Union for cleaner code

class StatusEnum(str, Enum):
    Pending = "Pending"
    Sent = "Sent"

class NotificationBase(BaseModel):
    patient_name: str
    message: str
    notification_time: datetime
    status: Optional[StatusEnum] = StatusEnum.Pending  # Use Optional for better readability

class NotificationCreate(NotificationBase):
    pass

class Notification(NotificationBase):
    id: int

    class Config:
        orm_mode = True
