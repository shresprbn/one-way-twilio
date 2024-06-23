from Utils.environmentVars import Environment_variables  
from twilio.rest import Client
from fastapi import APIRouter ,Depends
from model.model import Messagebody
from Utils.verifyToken import verify_token

router = APIRouter()
env_var = Environment_variables()

@router.post("/sendMessage")
def assemble(var:Messagebody):
    verify_token(var)

    account_sid = env_var.get_Account_Sid()
    client = Client(account_sid, var.auth_token)

    message = client.messages \
                .create(
                    body=var.message,
                    from_='+17206773138',
                    to=var.to
                )

    return message.sid
    
    # account_sid = env_var.get_Account_Sid()
    # auth_token = env_var.get_Auth_token()
    # client = Client(account_sid, auth_token)
    
    # message = client.messages \
    #             .create(
    #                 body=var.message,
    #                 from_='+17206773138',
    #                 to=var.to
    #             )

    # return{message.sid}