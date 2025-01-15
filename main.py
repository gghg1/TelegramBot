from instances import bot, dp
import handlers
import asyncio


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())