from aiogram import Dispatcher
from core import Router, Bot
from config import Config
from aiogram.fsm.storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(Config.BOT_TOKEN)
dp = Dispatcher(storage=storage)
router = Router()

dp.include_router(router)