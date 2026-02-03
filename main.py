import asyncio

# Force event loop (required for pytgcalls on Heroku)
try:
    asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

from pytgcalls import idle
from driver.veez import call_py, bot, user


async def start_bot():
    await bot.start()
    print("[INFO]: BOT & UBOT CLIENT STARTED !!")

    await call_py.start()
    print("[INFO]: PY-TGCALLS CLIENT STARTED !!")

    await idle()

    print("[INFO]: STOPPING BOT & USERBOT")
    await bot.stop()


if __name__ == "__main__":
    asyncio.run(start_bot())
