"""
All handlers
"""
from aiogram import types, Dispatcher

import config

from logger import get_logger

# from services.parser import parse_msg


CHAT_ID = config.RECIEVE_FROM
logger = get_logger(__name__)
dp = Dispatcher()


@dp.message(lambda msg: msg.chat.id == CHAT_ID)
async def any_msg(message: types.Message) -> None:
    """Recievs any msg and stores data about

    Args:
        message (types.Message): Message from user
    """

    logger.info('Recieved msg from %s', message.chat.id)

    # parse_msg(message)
