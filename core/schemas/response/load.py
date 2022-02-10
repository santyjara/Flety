from pydantic import BaseModel, PositiveInt


class LoadIdResponseModel(BaseModel):
    id: PositiveInt
