from sqlalchemy.orm import Session
from app import models, schemas

def get_notifications(db: Session):
    return db.query(models.Notification).all()

def create_notification(db: Session, notification: schemas.NotificationCreate):
    new_notification = models.Notification(**notification.dict())
    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)
    return new_notification

def get_notification(db: Session, notification_id: int):
    return db.query(models.Notification).filter(models.Notification.id == notification_id).first()

def update_notification_status(db: Session, notification_id: int, status: schemas.StatusEnum):
    notification = db.query(models.Notification).filter(models.Notification.id == notification_id).first()
    if notification:
        notification.status = status
        db.commit()
        db.refresh(notification)
    return notification
