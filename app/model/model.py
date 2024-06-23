from pydantic import BaseModel

class Messagebody(BaseModel):
    message : str
    restaurant : str
    to : str
    auth_token : str
    backend_token : str
