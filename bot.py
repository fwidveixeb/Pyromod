import os
from pyromod import listen
from pyrogram import Client

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")


bot = Client(":memory:",
      api_id=API_ID,
      api_hash=API_HASH,
      bot_token=BOT_TOKEN)
