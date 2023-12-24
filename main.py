"""
Entrypoint of bot
"""
from handlers import dp

from bot import bot


async def main() -> None:
    await dp.start_polling(bot)
