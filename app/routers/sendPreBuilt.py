from Utils.environmentVars import Environment_variables  
from twilio.rest import Client
from Utils.messageTemplate import MessageTemplate
from Utils.verifyToken import verify_token
from model.model import Messagebody
from fastapi import APIRouter

router = APIRouter()
env_var = Environment_variables()
mes_temp = MessageTemplate()


@router.post("/preBuiltMessage")
def preBuiltMessage(var:Messagebody):
    account_sid = env_var.get_Account_Sid()
    verify_token(var)
    client = Client(account_sid, var.auth_token)
    
    message = client.messages \
                .create(
                    body= mes_temp.returnMessage(restaurantName=var.restaurant, type=var.messagetype),
                    from_='+17206773138',
                    to=var.to
                )

    return{f"to : var.to {mes_temp.returnMessage(restaurantName=var.restaurant,type=var.messagetype)}"}

@router.post("/preBuiltMessage")
def assemble(var:Messagebody):
    account_sid = env_var.get_Account_Sid()
    verify_token(var)
    client = Client(account_sid, var.auth_token)
    msg,code = mes_temp.recoveryCode()
    
    message = client.messages \
                .create(
                    body= msg,
                    from_='+17206773138',
                    to=var.to
                )

    return{f"to : var.to {msg}"}