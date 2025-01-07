from sqlalchemy.orm import Session
from app import models, schemas

def get_patients(db: Session):
    return db.query(models.Patient).all()

def create_patient(db: Session, patient: schemas.PatientCreate):
    new_patient = models.Patient(**patient.dict())
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient

def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()

def delete_patient(db: Session, patient_id: int):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if patient:
        db.delete(patient)
        db.commit()
