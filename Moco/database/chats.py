from . import usersdb, chatsdb


async def get_chats() -> dict:
    """
    Fetch served users and chats from the database.
    Returns a dictionary containing lists of users and chats.
    """
    chats = []
    users = []

    async for chat in chatsdb.find({"chat_id": {"$lt": 0}}):
        chats.append(chat["chat_id"])
    async for user in usersdb.find({"user_id": {"$gt": 0}}):
        users.append(user["user_id"])

    return {
        "chats": chats,
        "users": users,
    }


async def add_user(user_id, username=None):
    """
    Adds a user to the database if they don't already exist.
    """
    if not await usersdb.find_one({"user_id": user_id}):
        await usersdb.insert_one({"user_id": user_id, "username": username})

async def add_chat(chat_id, title=None):
    """
    Adds a chat to the database if it doesn't already exist.
    """
    if not await chatsdb.find_one({"chat_id": chat_id}):
        await chatsdb.insert_one({"chat_id": chat_id, "title": title})
