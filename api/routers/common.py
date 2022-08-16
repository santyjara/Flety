from fastapi import APIRouter, Depends

from core import crud
from core.schemas.user import UserRolesResponse

router = APIRouter()


@router.get("/vehicle_types")
async def get_vehicle_types(
    return_sorted: bool = False,
    # user: UserRequestModel = Depends(Authenticator.get_request_user),
):
    vehicle_types = await crud.common.fetch_vehicle_types()
    if return_sorted:
        return sorted(vehicle_types, key=lambda x: x["name"].lower())
    return vehicle_types


@router.get("/load_types")
async def get_load_types(
    return_sorted: bool = False,
    # user: UserRequestModel = Depends(Authenticator.get_request_user),
):
    load_types = await crud.common.fetch_load_types()
    if return_sorted:
        return sorted(load_types)
    return load_types


@router.get("/trailer_types")
async def get_trailer_types(
    return_sorted: bool = False,
    # user: UserRequestModel = Depends(Authenticator.get_request_user),
):
    trailer_types = await crud.common.fetch_trailer_types()
    print(type(trailer_types))
    print(trailer_types)
    if return_sorted:
        return sorted(trailer_types)
    return trailer_types


@router.get("/user_roles", response_model=UserRolesResponse)
async def get_user_roles(
    return_sorted: bool = False,
    # user: UserRequestModel = Depends(Authenticator.get_request_user),
):
    user_roles = await crud.common.fetch_user_roles()
    if return_sorted:
        return sorted(user_roles)
    return user_roles
