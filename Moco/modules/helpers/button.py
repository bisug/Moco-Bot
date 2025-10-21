from pyrogram.types import InlineKeyboardButton

from config import BOT_USERNAME, OWNER_ID, SUPPORT_GROUP, UPDATES_CHANNEL 

DEV_ID = 7804972365 

STBUTTON = [
    [
        InlineKeyboardButton(
            text="✙ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✙",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="ᴏᴡɴᴇʀ", user_id=OWNER_ID),
        InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", user_id=DEV_ID),
    ],
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
    ],
    [
        InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}"),
        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/{UPDATES_CHANNEL}")
    ],
]

HELP_BACK_BUTTON = [
    [
        InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}"),
        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="back"),
    ],
]

PING_BUTTON = [
    [
        InlineKeyboardButton(
            text="✙ ᴀᴅᴅ ᴍᴇ 😘", 
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
        ),
        InlineKeyboardButton(
            text="sᴜᴘᴘᴏʀᴛ", 
            url=f"https://t.me/{SUPPORT_GROUP}"
        ),
    ],
]

