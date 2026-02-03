import asyncio
from config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME

# 🔥 FORCE EVENT LOOP BEFORE importing pytgcalls
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from pyrogram import Client
from pytgcalls import PyTgCalls

bot = Client(
    ":veez:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "program"},
)

user = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
)

# ✅ FIXED LINE — NO overload_quiet_mode
call_py = PyTgCalls(user)
