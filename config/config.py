from dotenv import load_dotenv
from os import getenv

load_dotenv()

class Config(object):
    BOT_TOKEN = getenv("BOT_TOKEN")
    ADMIN_ID = getenv("ADMIN_ID")