import telebot
from config import TOKEN
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Привет! Я бот для помощи в изучении языков! Чтобы узнать доступные команды напиши /help")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "Вам доступны команды: ")
