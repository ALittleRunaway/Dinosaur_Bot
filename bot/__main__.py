from aiogram import Bot
from aiogram import Dispatcher
from aiogram import executor
from aiogram import types

from .dinosaur import Dinosaur
from .logger import Logger
from .settings import settings

logger = Logger.get_logger()

bot = Bot(token=settings.API_TOKEN)
dp = Dispatcher(bot)

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
get_dino_button = types.KeyboardButton(text="Хочу динозавра! 🦕")
keyboard.add(get_dino_button)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """The entrypoint"""
    msg = """
Перивет! Видимо, ты очень любишь динозавров, если ты тут. 🤔
Чего же ты тогда ждешь? Скорее тыкай на кнопку и узнай о них всё-всё-всё!
    """
    await message.answer(msg, reply_markup=keyboard)


@dp.message_handler(regexp='Хочу динозавра! 🦕')
async def dinos(message: types.Message):
    """Get the dino!"""
    logger.info(f"{message.from_user.first_name} {message.from_user.last_name} {message.from_user.username}")
    dinosaur = Dinosaur()
    dinosaur.get_info()
    await message.answer_photo(dinosaur.img, caption=dinosaur.create_media_message())
    await message.answer(dinosaur.create_description_message())


if __name__ == '__main__':
    logger.info("The bot has started!")
    executor.start_polling(dp, skip_updates=True)
