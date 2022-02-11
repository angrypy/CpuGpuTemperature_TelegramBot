from config import tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, filters
from aiogram.utils import executor
from aiogram.utils.markdown import hbold, hlink
import logging

# Задаём уровень логирования
logging.basicConfig(level=logging.INFO)

bot = Bot(tg_bot_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start_command(message: types.Message):
    await message.reply("Привет, мы пупа и лупа, и это привет от бота!")

async def send_temperature_to_tg(message: types.Message):
    while True:
        cpu_temp = 1
        gpu_temp = 2
        await message.answer(f"Температура CPU: {cpu_temp}\nТемпература GPU: {gpu_temp} ")

if __name__ == "__main__":
    executor.start_polling(dp)


