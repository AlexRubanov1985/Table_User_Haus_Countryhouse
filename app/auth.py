import logging

from fastapi import APIRouter, HTTPException, Query, Body
from fastapi.params import Depends
from sqlmodel import Session, select
from typing import List

from .database import engine, get_session
from .models import User, Home, VacationHome, UserCreate, HomeCreate, VacationHomeCreate, UserRead, HomeRead, VacationHomeRead

logging.basicConfig(level=logging.DEBUG)
router = APIRouter()

@router.post("/users/", response_model=UserRead)
def create_user(user: UserCreate = Depends(UserCreate), session: Session = Depends(get_session)):
    try:
        db_user = User.from_orm(user)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user
    except Exception as e:
        logging.error(f"Error creating user: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: int, session: Session = Depends(get_session)):
    user = session.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user




@router.post("/homes/{user_id}", response_model=HomeRead)
def create_home(user_id: int, home: HomeCreate = Depends(HomeCreate), session: Session = Depends(get_session)):
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_home = Home.from_orm(home, update={"user_id": user_id})
    session.add(db_home)
    session.commit()
    session.refresh(db_home)
    return db_home



@router.post("/vocations/{user_id}", response_model=VacationHomeRead)
def create_home(user_id: int, home: VacationHomeCreate = Depends(VacationHomeCreate), session: Session = Depends(get_session)):
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_home = VacationHome.from_orm(home, update={"user_id": user_id})
    session.add(db_home)
    session.commit()
    session.refresh(db_home)
    return db_home




