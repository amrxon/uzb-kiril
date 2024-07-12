import asyncio
import logging
import sys
from os import getenv
from trans import latinOrcyrillic
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "6700545902:AAFZcQSETzdfgRlEIqBOnan3Ccr2vsHQpCU"


dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
   
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def latin(msg: Message):
    await msg.answer(latinOrcyrillic(msg.text))

@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main()) 