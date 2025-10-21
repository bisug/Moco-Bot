from typing import Callable, Union

from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, CallbackQuery

from Moco import app  


def is_admins(func: Callable) -> Callable:
    async def decorator(client: app, update: Union[Message, CallbackQuery]):
        # Determine context based on update type
        if isinstance(update, CallbackQuery):
            chat_id = update.message.chat.id
            user_id = update.from_user.id
        else:
            chat_id = update.chat.id
            user_id = update.from_user.id

        # Get user's status in the chat
        user = await client.get_chat_member(chat_id, user_id)
        
        # Check for admin privileges
        if user.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await func(client, update)
        
        # Non-admin response handling
        if isinstance(update, CallbackQuery):
            await update.answer("This command is restricted to admins only!", show_alert=True)
        else:
            await update.reply_text("This command is restricted to admins only!")

    return decorator
