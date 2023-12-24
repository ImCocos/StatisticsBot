"""
Bot from .env token
"""
from aiogram import Bot

import config


bot = Bot(token=config.BOT_TOKEN)
