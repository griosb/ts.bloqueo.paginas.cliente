from fastapi import APIRouter
from config.database import engine 
from sqlalchemy import select
from model.pagesModels import pageTable
from model.hostModel import hostTable
from templates.hostTemplate import HostTemplate

pageRouter = APIRouter()

@pageRouter.get("/")
def root():
    return {"message": "Block Pages"}

@pageRouter.post("/api/hostInfo")
def save_host(data_host: HostTemplate):
    with engine.connect() as conn:
        new_host=data_host.model_dump()
        conn.execute(hostTable.insert().values(new_host))
        conn.commit()
    return {'message': 'Success'}



@pageRouter.get("/api/block") #all the block pages
def pageBlock():
    with engine.connect() as conn:
         result = conn.execute(select(pageTable.c.Domain)).fetchall()
    return [r[0] for r in result]


