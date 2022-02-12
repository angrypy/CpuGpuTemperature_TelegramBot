from config import tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, filters
from aiogram.utils import executor
from aiogram.utils.markdown import hbold, hlink
import logging
from CpuGpuModule import getTemperature
import time


# Задаём уровень логирования
logging.basicConfig(level=logging.INFO)

bot = Bot(tg_bot_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start_command(message: types.Message):
    await message.reply("Привет, мы пупа и лупа, и это привет от бота!")

@dp.message_handler(commands="get_temp")
async def send_temperature_to_tg(message: types.Message):
    while True:
        await message.answer(f"{hbold('Температура CPU:')} {(getTemperature('CPU'))}\n{hbold('Температура GPU:')} {getTemperature('GPU')} ")
        time.sleep(60)

async def test_message(message: types.Message):
    await message.reply("Тестовое сообщение для теста бота!")

if __name__ == "__main__":
    executor.start_polling(dp)



