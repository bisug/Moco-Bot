from motor.motor_asyncio import AsyncIOMotorClient
import config 

Moco = AsyncIOMotorClient(config.MONGO_URL)
db = Moco["MOCO"] 
usersdb = db["users"]          
chatsdb = db["chats"]     
    
from .chats import *
from .admin import *
