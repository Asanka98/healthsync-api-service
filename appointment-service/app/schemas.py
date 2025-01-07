from pydantic import BaseModel
from datetime import datetime
from typing import Union

class AppointmentBase(BaseModel):
    patient_name: str
    doctor_name: str
    appointment_time: datetime
    reason: Union[str, None] = None 

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int

    class Config:
        orm_mode = True
