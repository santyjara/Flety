from fastapi import APIRouter

from core import crud
from core.schemas.load import LoadCreate

router = APIRouter()


@router.post("")
async def create_load(load_info: LoadCreate):

    await crud.load.create(load_info)
    return {"OK": 1}
