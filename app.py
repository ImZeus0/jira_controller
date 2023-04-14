from bot.loader import bot, storage , loop


async def on_shutdown(dp):
    await bot.close()
    await storage.close()


if __name__ == '__main__':
    from aiogram import executor
    from bot.handlers.start_handlers import dp
    executor.start_polling(dp,loop=loop,on_shutdown=on_shutdown)