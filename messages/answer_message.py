from abc import ABC
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from typing import Optional

class AnswerMessage(ABC):
    _text: str
    _markup: ReplyKeyboardMarkup | InlineKeyboardMarkup

    def __init__(self, text, markup: Optional[ReplyKeyboardMarkup | InlineKeyboardMarkup]):
        self.text = text
        
    @property
    def text(self): return self._text

    @text.setter
    def text(self, value: str):
        self._text = value

    @property
    def markup(self):
        return self._markup
    
    @markup.setter
    def markup(self, value: ReplyKeyboardMarkup | InlineKeyboardMarkup):
        self._markup = value

    def __str__(self):
        return self._text
        