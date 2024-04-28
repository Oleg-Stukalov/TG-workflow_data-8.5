import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import load_config
from handlers.user_handlers import user_router


async def main() -> None:

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    # Регистрируем роутеры в диспетчере
    dp.include_router(user_router)

    # workflow_data practice
    some_var_1 = 1
    some_var_2 = 'Some text'

    dp.workflow_data.update({'my_int_var': some_var_1, 'my_text_var': some_var_2})
    #print('Print from main.py dispatcher: ', dp.workflow_data)
    #print(dp['my_int_var'])
    #print(dp['my_text_var'])

    # Запускаем polling
    await dp.start_polling(bot)


asyncio.run(main())




###########
