import asyncio
import speedtest
from pyrogram import filters
from pyrogram.types import Message
from Moco import app


def run_speedtest():
    test = speedtest.Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    return test.results.dict()


@app.on_message(filters.command(["speedtest", "spt"]))
async def speedtest_function(_, message: Message):
    msg = await message.reply_text("🚀 **ʀᴜɴɴɪɴɢ sᴘᴇᴇᴅᴛᴇsᴛ...**")

    try:
        result = await asyncio.wait_for(asyncio.to_thread(run_speedtest), timeout=120)
    except asyncio.TimeoutError:
        return await msg.edit("⏳ **ᴛɪᴍᴇᴏᴜᴛ. ᴛʜᴇ sᴇʀᴠᴇʀ ᴅɪᴅ ɴᴏᴛ ʀᴇsᴘᴏɴᴅ.**")
    except Exception as e:
        return await msg.edit(f"❌ **ᴇʀʀᴏʀ:** `{str(e)}`")

    download = result["download"] / 1_000_000
    upload = result["upload"] / 1_000_000
    ping = result["ping"]
    isp = result["client"]["isp"]
    server = result["server"]["name"]
    country = result["server"]["country"]

    caption = (
        "📊 **sᴘᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs**\n\n"
        f"🏠 **ɪsᴘ:** `{isp}`\n"
        f"🌍 **sᴇʀᴠᴇʀ:** `{server}` ({country})\n"
        f"⚡ **ᴘɪɴɢ:** `{ping:.1f} ms`\n\n"
        f"⬇ **ᴅᴏᴡɴʟᴏᴀᴅ:** `{download:.2f} Mbps`\n"
        f"⬆ **ᴜᴘʟᴏᴀᴅ:** `{upload:.2f} Mbps`"
    )

    await message.reply_photo(photo=result["share"], caption=caption)
    await msg.delete() 
