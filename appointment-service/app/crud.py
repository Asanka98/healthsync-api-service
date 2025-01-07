from sqlalchemy.orm import Session
from app import models, schemas

def get_appointments(db: Session):
    return db.query(models.Appointment).all()

def create_appointment(db: Session, appointment: schemas.AppointmentCreate):
    new_appointment = models.Appointment(**appointment.dict())
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    return new_appointment

def get_appointment(db: Session, appointment_id: int):
    return db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()

def delete_appointment(db: Session, appointment_id: int):
    appointment = db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()
    if appointment:
        db.delete(appointment)
        db.commit()
