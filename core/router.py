from aiogram.dispatcher.router import Router as AiogramRouter
from aiogram.types import Message as AiogramMessage
from .types import Message, TelegramObject
from core import Bot
from typing import Any


class Router(AiogramRouter):
    """Кастомный Router, заменяющий стандартное сообщение на кастомное."""

    async def _propagate_event(
        self,
        update_type: str,
        event: TelegramObject,
        bot: Bot,
        **kwargs: Any
    ) -> Any:
        # Если событие — сообщение, заменяем его на кастомный Message
        if update_type == "message" and isinstance(event, AiogramMessage):
            # Преобразуем стандартное сообщение в кастомное
            event = Message(
                bot=bot,
                message_id=event.message_id,
                from_user=event.from_user,
                chat=event.chat,
                date=event.date,
                text=event.text,
                entities=event.entities,
                caption=event.caption,
                audio=event.audio,
                document=event.document,
                photo=event.photo,
                sticker=event.sticker,
                video=event.video,
                voice=event.voice,
                location=event.location,
                venue=event.venue,
                contact=event.contact,
                new_chat_members=event.new_chat_members,
                left_chat_member=event.left_chat_member,
                new_chat_title=event.new_chat_title,
                new_chat_photo=event.new_chat_photo,
                delete_chat_photo=event.delete_chat_photo,
                group_chat_created=event.group_chat_created,
                supergroup_chat_created=event.supergroup_chat_created,
                channel_chat_created=event.channel_chat_created,
                migrate_to_chat_id=event.migrate_to_chat_id,
                migrate_from_chat_id=event.migrate_from_chat_id,
                pinned_message=event.pinned_message,
                **kwargs
            )

        # Передаем событие в базовую реализацию
        return await super()._propagate_event(update_type=update_type, event=event, **kwargs)