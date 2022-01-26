from fastapi import FastAPI
from socket import gethostname
from pymongo import MongoClient


app = FastAPI()
mongo_client = MongoClient("mongodb://mongoadmin:secret@my_mongodb:27017")


@app.get("/")
async def index():
	return f"Host: {gethostname()}"


@app.get("/db")
async def get_db():
    try:
        mongo_client.server_info()
    except:
        return "MongoDB Connection Failed!"
    return "MongoDB Connected !"
