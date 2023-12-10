from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """ Define how error message is presented
    """
    message: str
