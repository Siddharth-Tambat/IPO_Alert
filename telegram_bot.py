import telebot
from dotenv import load_dotenv
import os

load_dotenv()
GROUP_ID = os.getenv('GROUP_ID')
bot = telebot.TeleBot(os.getenv('API_KEY'))


def ipo_alert(message, link):

    ipo_button = telebot.types.InlineKeyboardButton(text='Groww', url=link)

    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(ipo_button)
    bot.send_message(chat_id=GROUP_ID, text=message, reply_markup=keyboard)
    