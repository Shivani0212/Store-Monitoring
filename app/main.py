from fastapi import FastAPI
from .database import engine, Base
from .routers import report

app = FastAPI()

app.include_router(report.router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def root():
    return {"message": "Store Monitoring System"}
