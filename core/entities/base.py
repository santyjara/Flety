from pydantic import BaseModel, validate_model


class BaseCheckModel(BaseModel):
    def check(self):
        *_, validation_error = validate_model(self.__class__, self.__dict__)
        if validation_error:
            raise validation_error
