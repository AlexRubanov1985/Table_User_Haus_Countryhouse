from datetime import datetime
from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship




# Models
class HouseBase(SQLModel):
    address: str
    area: float
    build_date: Optional[datetime] = Field(default_factory=datetime.now)
    condition: bool
    Square: float

class Home(HouseBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    city: Optional[str] = None
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: "User" = Relationship(back_populates="homes")

class HouseRead(HouseBase):
    address: Optional[str] = Field()
    square: Optional[int] = Field()



class VacationHome(HouseBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: "User" = Relationship(back_populates="vacation_homes")

class VacationHomeRead(HouseBase):
    address: Optional[str] = Field()
    square: Optional[int] = Field()



class UserBase(SQLModel):
    first_name: str
    last_name: Optional[str] = None
    phone: int = Field(index=True)

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


    homes: List[Home] = Relationship(back_populates="user")
    vacation_homes: List[VacationHome] = Relationship(back_populates="user")


class HomeCreate(HouseBase):
    city: Optional[str] = None

class VacationHomeCreate(HouseBase):
    pass

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    pass

class HomeRead(HouseBase):
    city: Optional[str] = None

















