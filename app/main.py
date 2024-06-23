from fastapi import FastAPI
import os
from Utils.logger import setup_logger
from routers import sendMessage, sendPreBuilt


app = FastAPI(debug=True)
my_logger = setup_logger("../Logs","App_Log")

app.include_router(sendMessage.router)
app.include_router(sendPreBuilt.router)

@app.get("/")
def read_root():
    my_logger.info("User is in Root")
    return {"This is root"}

@app.get('/health_check')
def health_check():
    my_logger.info("User Conducted Health Check")
    return{"Healthy"}

@app.post("/greet")
def greet(name: str):
    return {f"Hello {name}"}

