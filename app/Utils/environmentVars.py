from dotenv import load_dotenv
import os

load_dotenv("../.venv/include/.env")

class Environment_variables:
    def __init__(self):
        self.ACCOUNT_SID = os.getenv("account_sid")
        self.AUTH_TOKEN = os.getenv("auth_token")
        self.BACKEND_TOKEN = os.getenv("backend_token")
        self.NUMBER = os.getenv("number")

    def get_Account_Sid(self):
        return self.ACCOUNT_SID
    
    def get_Auth_token(self):
        return self.AUTH_TOKEN
    
    def get_backend_token(self):
        return self.BACKEND_TOKEN
    
    def get_number(self):
        return self.NUMBER
