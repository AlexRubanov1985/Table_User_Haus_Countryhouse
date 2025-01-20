from fastapi import FastAPI
from sqlmodel import SQLModel, Session
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware


from .database import engine


middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    # with Session(engine) as session:
    #     if session.get(User, 1) is None:
    #         a=User(role='LLLLL')
    #         session.add(a)
    #         session.commit()
app = FastAPI(middleware=middleware, title='House and VacationHome', description='Новый проект', version='1')

from .auth import *



app.include_router(router, tags=["API | auth.py"], prefix="/api")
# app.include_router(enum_example_query.router, tags=["Enum Query Example "], prefix="/enum")

create_db_and_tables()