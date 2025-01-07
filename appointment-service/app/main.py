from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine, get_db

app = FastAPI()

# Ensure the database tables are created
models.Base.metadata.create_all(bind=engine)

@app.get("/appointments/", response_model=list[schemas.Appointment])
def get_appointments(db: Session = Depends(get_db)):
    return crud.get_appointments(db)

@app.post("/appointments/", response_model=schemas.Appointment)
def create_appointment(appointment: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    return crud.create_appointment(db, appointment)

@app.get("/appointments/{appointment_id}", response_model=schemas.Appointment)
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = crud.get_appointment(db, appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

@app.delete("/appointments/{appointment_id}", status_code=204)
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    crud.delete_appointment(db, appointment_id)
