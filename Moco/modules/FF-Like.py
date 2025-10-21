from Moco import app
from pyrogram import filters
import requests
import time
import random
from config import STICKER, LIKE_API_URL, LIKE_API_KEY, LOGGER_GROUP_ID

# ---------------- CONFIG ----------------

@app.on_message(filters.command("like") & filters.group)
async def like_command(client, message):
    try:
        loading_sticker = random.choice(STICKER)
        loading_msg = await message.reply_sticker(loading_sticker)
    except Exception:
        loading_msg = None

    start_time = time.time()
    args = message.text.split()

    # ===== VALIDATION =====
    if len(args) != 3:
        if loading_msg:
            await loading_msg.delete()
        return await message.reply_text(
            "ꜰʀᴇᴇ ꜰɪʀᴇ ʟɪᴋᴇ ʙᴏᴏꜱᴛᴇʀ!\n\n"
            "📘 ᴄᴏᴍᴍᴀɴᴅ ɢᴜɪᴅᴇ:\n"
            "`/like UID REGION`\n"
            "`/like REGION UID`\n\n"
            "ᴇxᴀᴍᴘʟᴇ:\n`/like 12345678 BD`\n"
            "ᴇxᴀᴍᴘʟᴇ:\n`/like BD 12345678`"
        )

    arg1, arg2 = args[1], args[2]

    # ===== DETECT UID AND REGION =====
    if arg1.isdigit():
        uid, input_region = arg1, arg2.upper()
    elif arg2.isdigit():
        uid, input_region = arg2, arg1.upper()
    else:
        if loading_msg:
            await loading_msg.delete()
        return await message.reply_text("⚠️ **ɪɴᴠᴀʟɪᴅ ᴀʀɢᴜᴍᴇɴᴛꜱ!** ᴏɴᴇ ᴍᴜꜱᴛ ʙᴇ ᴀ ɴᴜᴍᴇʀɪᴄ ᴜɪᴅ.")

    # ===== REGION NORMALIZATION =====
    if input_region == "IND":
        region = "IND"
    elif input_region in {"BR", "US", "SAC", "NA"}:
        region = "BR"
    else:
        region = "BD"

    # ===== API REQUEST =====
    url = f"{API_URL}/like?uid={uid}&server_name={region}&key={API_KEY}"
    try:
        response = requests.get(url, timeout=60)
        data = response.json()
    except requests.exceptions.Timeout:
        if loading_msg:
            await loading_msg.delete()
        return await message.reply_text("⏳ **ʀᴇǫᴜᴇꜱᴛ ᴛɪᴍᴇᴅ ᴏᴜᴛ!** ᴀᴘɪ ᴛᴏᴏ ꜱʟᴏᴡ.")
    except requests.exceptions.RequestException:
        if loading_msg:
            await loading_msg.delete()
        return await message.reply_text("🚫 **ᴀᴘɪ ᴜɴʀᴇᴀᴄʜᴀʙʟᴇ!** ᴄʜᴇᴄᴋ ꜱᴇʀᴠᴇʀ ꜱᴛᴀᴛᴜꜱ.")
    except ValueError:
        if loading_msg:
            await loading_msg.delete()
        return await message.reply_text("⚠️ **ɪɴᴠᴀʟɪᴅ ʀᴇꜱᴘᴏɴꜱᴇ ꜰʀᴏᴍ ᴀᴘɪ.**")

    elapsed = round(time.time() - start_time, 2)

    # ===== HANDLE RESPONSE =====
    if "error" in data:
        err = data["error"]
        if "Invalid API key" in err:
            text = "🚫 **ɪɴᴠᴀʟɪᴅ ᴀᴘɪ ᴋᴇʏ.** ᴄᴏɴᴛᴀᴄᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ."
        elif "Failed to retrieve initial player info" in err:
            text = f"❌ ᴛʜɪs ᴜɪᴅ {uid} ᴅᴏᴇs ɴᴏᴛ ᴇxɪsᴛ ɪɴ ᴛʜᴇ ɢᴀʀᴇɴᴀ ᴅᴀᴛᴀʙᴀsᴇ ᴏʀ ʜᴀs ɴᴏᴛ ғᴜʟʟʏ ʀᴇɢɪsᴛᴇʀᴇᴅ ɪɴ ᴀ ʀᴇɢɪᴏɴ."
        else:
            text = f"⚠️ **ᴛᴏᴋᴇɴ ɪs ʙᴇɪɴɢ ʀᴇғʀᴇsʜᴇᴅ ғᴏʀ {input_region}, ɪᴛ'ʟʟ ᴛᴀᴋᴇ sᴏᴍᴇ ᴛɪᴍᴇ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 𝟻-𝟷𝟶 ᴍɪɴᴜᴛᴇs.**"
    else:
        request_ok = data.get("RequestSuccessful", False)
        player = data.get("PlayerNickname", "Unknown")
        likes_before = data.get("LikesbeforeCommand", "N/A")
        likes_after = data.get("LikesafterCommand", "N/A")
        given = data.get("LikesGivenByAPI", 0)

        if request_ok:
            text = (
                f"✅ **ʟɪᴋᴇs ꜱᴇɴᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ!**\n\n"
                f"👤 **ᴘʟᴀʏᴇʀ:** `{player}`\n"
                f"🆔 **ᴜɪᴅ:** `{uid}`\n"
                f"🌍 **ʀᴇɢɪᴏɴ:** `{input_region}`\n"
                f"💖 **ʟɪᴋᴇs ʙᴇꜰᴏʀᴇ:** `{likes_before}`\n"
                f"🔢 **ʟɪᴋᴇs ɢɪᴠᴇɴ:** `{given}`\n"
                f"💫 **ʟɪᴋᴇs ᴀꜰᴛᴇʀ:** `{likes_after}`\n"
                f"⏱️ **ʀᴇꜱᴘᴏɴꜱᴇ:** `{elapsed}s`"
            )
        else:
            text = (
                f"⚠️ **ᴜɪᴅ {uid} ʜᴀꜱ ᴀʟʀᴇᴀᴅʏ ʀᴇᴄᴇɪᴠᴇᴅ ᴍᴀx ʟɪᴋᴇꜱ ꜰᴏʀ ᴛᴏᴅᴀʏ.**\n"
                f"➡️ **ᴛʀʏ ᴀɢᴀɪɴ ᴛᴏᴍᴏʀʀᴏᴡ ᴏʀ ᴛʀʏ ᴀ ᴅɪꜰꜰᴇʀᴇɴᴛ ᴜɪᴅ.**\n\n"
                f"👤 **ᴘʟᴀʏᴇʀ:** `{player}`\n"
                f"🆔 **ᴜɪᴅ:** `{uid}`\n"
                f"🌍 **ʀᴇɢɪᴏɴ:** `{input_region}`\n"
                f"💖 **ʟɪᴋᴇs ʙᴇꜰᴏʀᴇ:** `{likes_before}`\n"
                f"💫 **ʟɪᴋᴇs ᴀꜰᴛᴇʀ:** `{likes_after}`\n"
                f"⏱️ **ʀᴇꜱᴘᴏɴꜱᴇ:** `{elapsed}s`"
            )

    if loading_msg:
        await loading_msg.delete()

    await message.reply_text(text, disable_web_page_preview=True)

    # ===== LOGGER =====
    if data.get("RequestSuccessful") and message.chat.id != LOGGER_GROUP_ID:
        try:
            log_text = (
                f"✅ **ʟɪᴋᴇs ꜱᴇɴᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ!**\n\n"
                f"👤 **ᴘʟᴀʏᴇʀ:** `{player}`\n"
                f"🎮 **ᴜɪᴅ:** `{uid}`\n"
                f"🌍 **ʀᴇɢɪᴏɴ:** `{input_region}`\n"
                f"💖 **ʟɪᴋᴇs ʙᴇꜰᴏʀᴇ:** `{likes_before}`\n"
                f"🔢 **ʟɪᴋᴇs ɢɪᴠᴇɴ:** `{given}`\n"
                f"💫 **ʟɪᴋᴇs ᴀꜰᴛᴇʀ:** `{likes_after}`\n"
                f"⏱️ **ʀᴇꜱᴘᴏɴꜱᴇ:** `{elapsed}s`\n\n"
                f"👤 **ᴜꜱᴇʀ:** {message.from_user.mention}\n"
                f"🆔 **ᴜꜱᴇʀ ɪᴅ:** `{message.from_user.id}`\n"
                f"💬 **ᴄʜᴀᴛ:** `{message.chat.title}`"
            )
            await client.send_message(LOGGER_GROUP_ID, log_text)
        except Exception:
            pass
