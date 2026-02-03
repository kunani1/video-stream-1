import asyncio

# Force event loop BEFORE pytgcalls import
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from pytgcalls import idle
from driver.veez import call_py, bot, user


async def start_bot():
    await bot.start()
    print("[INFO]: BOT & USER STARTED")

    await call_py.start()
    print("[INFO]: PYTGCALLS STARTED")

    await idle()

    print("[INFO]: STOPPING BOT")
    await bot.stop()


if __name__ == "__main__":
    asyncio.run(start_bot())
