"""
Config
"""
import os

import logging

from dotenv import load_dotenv


load_dotenv(os.path.join(os.getcwd(), '.env'))

DEBUG = True

BOT_TOKEN = os.environ['BOT_TOKEN']

CHAT_ID = os.environ['CHAT_ID']
TEST_CHAT_ID = os.environ['TEST_CHAT_ID']
RECIEVE_FROM = TEST_CHAT_ID if DEBUG else TEST_CHAT_ID

DEBUG_LEVEL = logging.DEBUG
NORMAL_LEVEL = logging.INFO
LOG_LEVEL = DEBUG_LEVEL if DEBUG else NORMAL_LEVEL
logging.basicConfig(level=LOG_LEVEL)

DB_NAME = os.environ['DB_NAME']
DB_USER_NAME = os.environ['DB_USER_NAME']
DB_HOST = os.environ['DB_HOST']
DB_PORT = os.environ['DB_PORT']
DB_PASSWORD = os.environ['DB_PASSWORD']
