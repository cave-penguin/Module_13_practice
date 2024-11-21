from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor


admin = [369921677]

# Укажите ваш токен бота
API_TOKEN = "7887074932:AAGWX-FV2p_foXbF05fSXiAHuZ6LN8_zo8g"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    await message.answer(f"Ваш ID: {user_id}")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
