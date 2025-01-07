from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine, get_db

app = FastAPI()

# Ensure the database tables are created
models.Base.metadata.create_all(bind=engine)

@app.get("/notifications/", response_model=list[schemas.Notification])
def get_notifications(db: Session = Depends(get_db)):
    return crud.get_notifications(db)

@app.post("/notifications/", response_model=schemas.Notification)
def create_notification(notification: schemas.NotificationCreate, db: Session = Depends(get_db)):
    return crud.create_notification(db, notification)

@app.get("/notifications/{notification_id}", response_model=schemas.Notification)
def get_notification(notification_id: int, db: Session = Depends(get_db)):
    notification = crud.get_notification(db, notification_id)
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification

@app.put("/notifications/{notification_id}/status", response_model=schemas.Notification)
def update_notification_status(notification_id: int, status: schemas.StatusEnum, db: Session = Depends(get_db)):
    notification = crud.update_notification_status(db, notification_id, status)
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification
