from fastapi import  HTTPException
from Utils.environmentVars import Environment_variables

env_var = Environment_variables()

def verify_token(token):
    
    if token.auth_token != env_var.get_Auth_token():
        raise HTTPException(status_code=401, detail="The auth_token you provided is wrong")
    
    if token.backend_token != env_var.get_backend_token():
        raise HTTPException(status_code=401, detail="The backend_token you provided is wrong")