import asyncio
from aiogram import F, Bot, Dispatcher

from App.handlers import router


async def main():
    bot = Bot(token='7305622150:AAHAncpF0N1D2mnzhwRI_aZ7ZGW25oAkyD4')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot is off')