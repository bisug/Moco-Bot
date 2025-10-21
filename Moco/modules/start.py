import asyncio
import random

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatType

from config import IMG, BOT_USERNAME, SUPPORT_GROUP, OWNER_ID, UPDATES_CHANNEL
from Moco import app
from Moco.database import add_user

from Moco.modules.helpers import (
    START,
    STBUTTON,
    HELP_READ,
    HELP_BACK_BUTTON
)


# ─── COMMAND HANDLERS ───────────────────────────────────
@app.on_message(filters.command("start") & ~filters.bot)
async def start(client, m: Message):
    if not m.from_user:
        return await m.reply_text("😘")

    user_id = m.from_user.id

    # Private chat
    if m.chat.type == ChatType.PRIVATE:
        await add_user(user_id, m.from_user.username or None)
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=START,
            reply_markup=InlineKeyboardMarkup(STBUTTON),
        )
    else:  
        await m.reply_text(
            text=f"ʜᴇʏ [{m.from_user.first_name}](tg://user?id={user_id})!\n{START}",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "➕ Add Me",
                        url=f"https://t.me/{client.me.username}?startgroup=true"
                    ),
                    InlineKeyboardButton(
                        "💬 Support",
                        url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ]
            ])
        )


@app.on_message(filters.command("help"))
async def help_command(client, message):
    await message.reply_photo(
        photo=random.choice(IMG),
        caption=HELP_READ,
        reply_markup=InlineKeyboardMarkup(HELP_BACK_BUTTON)
    )


# ─── UNIFIED CALLBACK HANDLER ───────────────────────────
@app.on_callback_query()
async def callback_handler(client, cq):
    data = cq.data
    await cq.answer() 

    if data == "help":
        try:
            await cq.message.edit_caption(
                caption=HELP_READ,
                reply_markup=InlineKeyboardMarkup(HELP_BACK_BUTTON)
            )
        except Exception:
            await cq.message.edit_text(
                HELP_READ,
                reply_markup=InlineKeyboardMarkup(HELP_BACK_BUTTON)
            )

    elif data == "back":
        try:
            await cq.message.edit_caption(
                caption=START,
                reply_markup=InlineKeyboardMarkup(STBUTTON),
            )
        except Exception:
            await cq.message.edit_text(
                text=START,
                reply_markup=InlineKeyboardMarkup(STBUTTON),
            )

    else:
      
        await cq.answer(f"Unknown action: {data}", show_alert=True)
