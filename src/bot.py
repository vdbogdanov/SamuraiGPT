"""
Telegram bot
"""
import os
from aiogram import Bot, Dispatcher, executor, types
from openai_api import ChatGPT

TELEGRAM_BOT_API_KEY = os.getenv("TELEGRAM_BOT_API_KEY")
TELEGRAM_BOT_USERS = [os.getenv("TG_USER1")]
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = Bot(token=TELEGRAM_BOT_API_KEY)
dp = Dispatcher(bot)
chatgpt = ChatGPT(OPENAI_API_KEY)

accepted_users = lambda message: message.from_user.username not in TELEGRAM_BOT_USERS


@dp.message_handler(accepted_users, content_types=["any"])
async def handle_unwanted_users(message: types.Message):
    """
    Denial of access for unauthorized users
    """
    await message.answer("Sorry, the bot only works for approved users.")
    return


@dp.message_handler()
async def send_welcome(message: types.Message):
    """
    Reply on request to ChatGPT API
    """
    message_text = chatgpt.request(message.text)

    await bot.send_chat_action(message.chat.id, types.ChatActions.TYPING)
    await message.answer(message_text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
