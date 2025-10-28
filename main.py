from fastapi import FastAPI
from router.router import pageRouter

app = FastAPI()

app.include_router(pageRouter)
