from fastapi import FastAPI
from core.config import settings 


app=FastAPI(title=settings.app_name,version=settings.app_version,debug=settings.debug)

@app.get("/")
async def root():
    return {"message": "Hello World"}