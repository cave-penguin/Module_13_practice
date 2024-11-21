import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from aiogram import Bot, Dispatcher

from config import *
from keyboards import start_kb, catalog_kb, buy_kb
import text

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands='start')
async def start(message):
    await message.answer(f"Welcome, {message.from_user.username}. " +
                         text.start,
                         reply_markup=start_kb)

# message.answer_photo
# message.answer_video
# message.answer_file


@dp.message_handler(text='about')
async def info(message):
    with open('files/kisspng-penguin-tux.png', 'rb') as img:
        await message.answer_photo(img, text.about, reply_markup=start_kb)


@dp.message_handler(text='cost')
async def price(message):
    await message.answer('What are you interested in?', reply_markup=catalog_kb)


@dp.callback_query_handler(text='medium')
async def buy_m(call):
    await call.message.answer(text.Mgame, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='big')
async def buy_l(call):
    await call.message.answer(text.Lgame, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='mega')
async def buy_xl(call):
    await call.message.answer(text.XLgame, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='other')
async def buy_other(call):
    await call.message.answer(text.other, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='back_to_catalog')
async def back(call):
    await call.message.answer('What are you interested in?',
                          reply_markup=catalog_kb)
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
