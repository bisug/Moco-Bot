import os
import importlib
import subprocess
import asyncio

from pyrogram import idle

from Moco import app
from Moco.modules import ALL_MODULES
from config import WEB_APP  

async def boot():
    await app.start()

    for module in ALL_MODULES:
        importlib.import_module(f"Moco.modules.{module}")

    if WEB_APP:
        subprocess.Popen(['python3', 'app.py'])

    await idle()
    await app.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(boot())
