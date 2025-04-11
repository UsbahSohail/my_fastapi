from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, oauth2
from app.utils import verify_password

from app.database import get_db
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
                   tags=["Authentication"])

@router.post("/login")
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.email == user_credentials.username).first()  # Fetch user by email with improved clarity


        if not user or not verify_password(user_credentials.password, user.password):

            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

        access_token = oauth2.create_access_token(data={"user_id": user.id})
        return {"access_token": access_token, "token_type": "bearer", "user_id": user.id}

    except Exception as e:
        print(f"Error during login: {e}")  # Improved logging for debugging




        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
