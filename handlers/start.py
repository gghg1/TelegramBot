from instances import router
from aiogram.filters import Command
from core.types import Message
from messages import AnswerMessage


@router.message(Command("start"))
async def start(message: Message):

    start_message = AnswerMessage(
        text="Добро пожаловать! Это стартовое сообщение.",
        markup=None,  # Или добавьте клавиатуру
    )
    await message.answer(start_message)
