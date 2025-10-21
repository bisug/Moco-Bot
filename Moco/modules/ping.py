import platform
import psutil
import random
import time
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, Message

from config import IMG
from Moco import app
from Moco.modules.helpers import PING_BUTTON

start_time = datetime.now()
process = psutil.Process()


def format_uptime(delta):
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return (f"{days}d " if days else "") + f"{hours:02}h {minutes:02}m {seconds:02}s"


def status_emoji(percent):
    return "🟢" if percent < 50 else "🟡" if percent < 80 else "🔴"


@app.on_message(filters.command("ping"))
async def ping(client, message: Message):
    # Measure message latency
    start = time.perf_counter()
    sent = await message.reply("📡 Pinging...")
    msg_ping = (time.perf_counter() - start) * 1000
    await sent.delete()

    # Uptime
    uptime = format_uptime(datetime.now() - start_time)

    # System Stats
    ram = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=0.5)  # quick stable read

    # Bot Process Stats
    with process.oneshot():
        proc_mem = process.memory_info().rss / (1024**2)  # MB
        threads = process.num_threads()

    caption = (
        f"✨ **System Status** ✨\n\n"
        f"📡 **Ping:** `{msg_ping:.2f} ms`\n"
        f"⏳ **Uptime:** `{uptime}`\n\n"
        f"🧠 **RAM:** `{ram.percent}%` {status_emoji(ram.percent)}\n"
        f"🖥️ **CPU:** `{cpu}%` {status_emoji(cpu)}\n\n"
        f"⚙️ **Bot Memory:** `{proc_mem:.2f} MB`\n"
        f"🧵 **Threads:** `{threads}`\n\n"
        f"🧰 **OS:** `{platform.system()} {platform.release()}`\n"
        f"🐍 **Python:** `{platform.python_version()}`\n"
    )

    await message.reply_photo(
        photo=random.choice(IMG),
        caption=caption,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup(PING_BUTTON),
    )
