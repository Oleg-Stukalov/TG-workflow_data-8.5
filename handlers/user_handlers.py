from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message

user_router = Router()


# Этот хэндлер будет срабатывать на команду "/start" -
# добавлять пользователя в базу данных, если его там еще не было
# и отправлять ему приветственное сообщение
@user_router.message(CommandStart())
async def process_start_command(message: Message, my_int_var, my_text_var):
    print('user_handlers.py "process_start_command" handler: ', my_int_var)
    print('user_handlers.py "process_start_command" handler: ', my_text_var)
    await message.answer(my_text_var)
