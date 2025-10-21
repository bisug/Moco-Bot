from Moco import db

usersdb = db.users


async def is_served_user(user_id: int) -> bool:
    """Checks if the user is served (exists in the database)."""
    user = await usersdb.find_one({"user_id": user_id})
    return user is not None


async def get_served_users() -> list:
    """Returns a list of all served users."""
    users_list = []
    async for user in usersdb.find({"user_id": {"$gt": 0}}):
        users_list.append(user)
    return users_list


async def add_served_user(user_id: int):
    """Adds a new user to the served list."""
    is_served = await is_served_user(user_id)
    if is_served:
        return
    return await usersdb.insert_one({"user_id": user_id})
