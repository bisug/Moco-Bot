import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait, RPCError
from pyrogram.types import Message
from Moco import app
from Moco.database import get_chats
from config import OWNER_ID


@app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast_message(_, message: Message):
    reply = message.reply_to_message
    args = message.text.split()
    
    # Detect pin flag
    pin_flag = "-pin" in args
    text = " ".join(arg for arg in args[1:] if arg != "-pin") if len(args) > 1 else None

    if not reply and not text:
        return await message.reply("❗ Please reply to a message or add text to broadcast.")

    # Load chats
    data = await get_chats()
    recipients = data["chats"] + data["users"]
    total = len(recipients)

    # Start broadcasting
    progress = await message.reply(f"📡 Broadcasting to **{total}** chats...\nProgress: `0%`")

    sent_groups, sent_users, failed, pinned = 0, 0, 0, 0

    for count, chat_id in enumerate(recipients, start=1):
        try:
            # Send or copy message
            if reply:
                sent_msg = await reply.copy(chat_id)
            else:
                sent_msg = await app.send_message(chat_id, text=text)

            # If group and pinning enabled
            if chat_id < 0:
                if pin_flag:
                    try:
                        await sent_msg.pin(disable_notification=True)
                        pinned += 1
                    except:
                        pass
                sent_groups += 1
            else:
                sent_users += 1

        except FloodWait as fw:
            await asyncio.sleep(fw.value + 1)
            continue
        except RPCError:
            failed += 1
        except Exception:
            failed += 1

        # Update progress every 10 messages
        if count % 10 == 0 or count == total:
            percent = int((count / total) * 100)
            try:
                await progress.edit(f"📡 Broadcasting...\nProgress: `{percent}%`")
            except:
                pass

        await asyncio.sleep(0.2)  # Control rate

    # Final report
    await progress.edit(
        f"✅ **Broadcast Completed**\n\n"
        f"👥 Groups Reached: `{sent_groups}`\n"
        f"🧑‍💻 Users Reached: `{sent_users}`\n"
        f"📌 Messages Pinned: `{pinned}`\n"
        f"❌ Failed: `{failed}`"
    )
