from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, database, auth

router = APIRouter()

@router.post("/register")
def register(email: str, password: str, db: Session = Depends(database.SessionLocal)):
    user = models.User(email=email, password=auth.hash_password(password))
    db.add(user)
    db.commit()
    return {"message": "User created"}

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(database.SessionLocal)):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user or not auth.verify_password(password, user.password):
        return {"error": "Invalid credentials"}

    token = auth.create_token({"user_id": user.id})
    return {"access_token": token}