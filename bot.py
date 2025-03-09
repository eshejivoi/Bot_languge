import telebot
from config import TOKEN
bot = telebot.TeleBot(TOKEN)
from telebot.types import ReplyKeyboardMarkup, KeyboardButton



TOKEN = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)
translator = Translator()



# Main menu
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(KeyboardButton("✨ Переводчик"))
main_menu.add(KeyboardButton("💡 Изучение языка"))

# Language selection menu
lang_menu = ReplyKeyboardMarkup(resize_keyboard=True)
langs = {"🇫🇷 Французский": "fr", "🇮🇹 Итальянский": "it", 
         "🇩🇪 Немецкий": "de", "🇪🇸 Испанский": "es", "🇬🇧 Английский": "en"}
for lang in langs.keys():
    lang_menu.add(KeyboardButton(lang))

user_mode = {}
user_lang = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Выбери режим:", reply_markup=main_menu)

@bot.message_handler(func=lambda message: message.text in ["✨ Переводчик", "💡 Изучение языка"])
def choose_mode(message):
    user_mode[message.chat.id] = message.text
    bot.send_message(message.chat.id, "Выбери язык:", reply_markup=lang_menu)

@bot.message_handler(func=lambda message: message.text in langs.keys())
def choose_language(message):
    user_lang[message.chat.id] = langs[message.text]
    if user_mode[message.chat.id] == "✨ Переводчик":
        bot.send_message(message.chat.id, "Отправь мне текст для перевода.")


@bot.message_handler(func=lambda message: message.chat.id in user_lang)
def handle_text(message):
    if user_mode[message.chat.id] == "✨ Переводчик":
        translated_text = translate_text(message.text, user_lang[message.chat.id])
        bot.send_message(message.chat.id, f"Перевод: {translated_text}")

bot.polling()
