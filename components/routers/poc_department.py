
from fastapi import APIRouter

from models.orm_models.poc_department import PoCDepartment

router = APIRouter()

@router.get("/all_departments_info/")
async def get_all_departments():
    return await PoCDepartment.all().values()