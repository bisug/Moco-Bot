from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from Moco import app, BOT_USERNAME, SUPPORT_GROUP
from Moco.database import get_chats


@app.on_message(filters.command("stats"))
async def stats(client, message: Message):
    try:
        data = await get_chats()
        total_users = len(data["users"])
        total_chats = len(data["chats"])

        await message.reply_text(
            f"""**{(await client.get_me()).first_name} Bot Statistics**

Users   : {total_users}
Groups  : {total_chats}""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Add Me", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                        InlineKeyboardButton("Updates", url=f"https://t.me/{SUPPORT_GROUP}")
                    ]
                ]
            )
        )
    except Exception as e:
        await message.reply_text(f"❌ Failed to fetch stats.\n`{str(e)}`")
