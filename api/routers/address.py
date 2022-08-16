from datetime import datetime

from fastapi import APIRouter, Depends

from core import crud
from core.entities import Load
from core.schemas.address import AddressCreate

router = APIRouter()


@router.post("")
async def create_address(
    obj_in: AddressCreate,
    # user: UserRequestModel = Depends(Authenticator.get_request_user),
):
    user_id = 1  # TODO get the real user id

    obj_in.user_id = user_id
    obj_in.check()

    _id = await crud.address.create(obj_in)

    print("answer")
    print(_id)

    return {"id": _id}
