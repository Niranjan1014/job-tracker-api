from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, database

router = APIRouter()

@router.post("/jobs")
def create_job(title: str, company: str, status: str, db: Session = Depends(database.SessionLocal)):
    job = models.Job(title=title, company=company, status=status)
    db.add(job)
    db.commit()
    return {"message": "Job added"}

@router.get("/jobs")
def get_jobs(db: Session = Depends(database.SessionLocal)):
    return db.query(models.Job).all()