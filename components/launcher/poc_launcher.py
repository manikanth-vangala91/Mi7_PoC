from datetime import date, datetime
from fastapi import FastAPI

from components.routers import poc_department, poc_employee
from models.orm_models.poc_department import PoCDepartment
from models.orm_models.poc_employee import PoCEmployee
from utils.database.poc_db_config import init_db

app = FastAPI()

@app.on_event("startup")
async def startup():
  is_db_initialised = await init_db()
  print(f"startup is_db_initialised : {is_db_initialised}")

app.include_router(poc_employee.router)
app.include_router(poc_department.router)