
from datetime import date, datetime
from fastapi import APIRouter

from models.orm_models.poc_employee import PoCEmployee

router = APIRouter()

@router.get("/all_employees_info/")
async def get_all_employees():
    employees = await PoCEmployee.all().values()
    for row in employees:
        for k, v in row.items():
            if isinstance(v, (date, datetime)):
                row[k] = v.isoformat()
    return employees