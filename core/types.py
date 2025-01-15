import aiogram.types
from messages import AnswerMessage
from aiogram.types import Message as AiogramMessage


class Message(AiogramMessage):
    bot = None

    async def answer(
        self,
        message_answer: 'AnswerMessage',
        parse_mode=None,
        entities=None,
        link_preview_options=None,
        disable_notification=None,
        protect_content=None,
        allow_paid_broadcast=None,
        message_effect_id=None,
        reply_parameters=None,
        allow_sending_without_reply=None,
        disable_web_page_preview=None,
        reply_to_message_id=None,
        **kwargs,
    ):
        # Проверяем, является ли message_answer текстом
        if isinstance(message_answer, str):
            text_to_send = message_answer
        elif hasattr(message_answer, 'text') and isinstance(message_answer.text, str):
            text_to_send = message_answer.text
        else:
            raise TypeError(f"Неверный тип данных для 'text'. Ожидалась строка, получено: {type(message_answer)}")

        return await super().answer(
            text=text_to_send,
            parse_mode=parse_mode,
            entities=entities,
            link_preview_options=link_preview_options,
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            message_effect_id=message_effect_id,
            reply_parameters=reply_parameters,
            reply_markup=message_answer.markup if hasattr(message_answer, 'markup') else None,
            allow_sending_without_reply=allow_sending_without_reply,
            disable_web_page_preview=disable_web_page_preview,
            reply_to_message_id=reply_to_message_id,
            **kwargs,
        )


class CallBackQuery(aiogram.types.CallbackQuery):
    pass


class ReplyKeyboardMarkup(aiogram.types.ReplyKeyboardMarkup):
    pass


class InlineKeyboardMarkup(aiogram.types.InlineKeyboardMarkup):
    pass


class KeyboardButton(aiogram.types.KeyboardButton):
    pass


class TelegramObject(aiogram.types.TelegramObject):
    pass

