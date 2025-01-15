from .answer_message import AnswerMessage
from aiogram_calendar import SimpleCalendar
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


calendar_markup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📅 Выбрать дату", callback_data="calendar_start")]
])

start_message = AnswerMessage(
    text=f"""
    Привет! 👋 Ты хочешь записаться на маникюр? ✨
    Напиши дату в формате ДД.ММ (например, 15.01), и я тебя запишу!
    
    Или выбери дату с помощью календаря ниже. 👇

    Если возникнут вопросы, используй команду /help.
    Для перезапуска бота напиши /restart.""",
    markup=calendar_markup
)