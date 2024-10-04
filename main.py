import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply('Привет!')
    await message.answer_photo(photo='https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2c/97/1d/72/caption.jpg',
                               caption='Классный ресторан астория\nОн крут. ')


@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Команды в боте:\n/start\n/help')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO) # Подключение логирования
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')