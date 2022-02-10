from datetime import datetime

from fastapi import APIRouter

from core.entities import Load
from core.schemas.request import LoadRequestModel
from core.schemas.response import LoadIdResponseModel

router = APIRouter()


@router.post("/load", response_model=LoadIdResponseModel)
async def create_load(load_info: LoadRequestModel):
    load_info = load_info.dict()
    load_info["created_on"] = datetime.utcnow()
    load_info["created_by"] = "user_test"
    print(load_info)
    load = Load.parse_obj(load_info)
    print(load)

    return LoadIdResponseModel(id=1)
