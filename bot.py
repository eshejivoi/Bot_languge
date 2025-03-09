import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from translator.translator import Translator

from config import TOKEN
from logic import test_questions, translate_text
import random

bot = telebot.TeleBot(TOKEN)
user_states = {}





translator = Translator()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для помощи в изучении языков! Чтобы узнать доступные команды напиши /help")


@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Вам доступны команды:\n"
        "/test - Начать тест для определения уровня английского\n"
        "/help - Показать список команд"
    )
    bot.reply_to(message, help_text)


@bot.message_handler(commands=['test'])
def start_test(message):
    user_id = message.from_user.id
    all_questions = [q for level in test_questions.values() for q in level]
    selected_questions = random.sample(all_questions, 5)

    user_states[user_id] = {
        'questions': selected_questions,
        'current_question': 0,
        'correct': 0
    }

    send_question(user_id)


def send_question(user_id):
    user_data = user_states.get(user_id)
    if not user_data:
        return

    current_idx = user_data['current_question']
    if current_idx >= len(user_data['questions']):
        calculate_result(user_id)
        return

    question_text, options = user_data['questions'][current_idx]
    correct_options = options[0]
    wrong_option = options[1]
    all_answers = correct_options + [wrong_option]
    random.shuffle(all_answers)

    markup = telebot.types.InlineKeyboardMarkup()
    for answer in all_answers:
        markup.add(telebot.types.InlineKeyboardButton(text=answer, callback_data=answer))

    bot.send_message(user_id, f"Вопрос {current_idx + 1}:\n{question_text}", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_answer(call):
    user_id = call.from_user.id
    user_data = user_states.get(user_id)
    if not user_data:
        bot.answer_callback_query(call.id, "Тест не активен.")
        return

    current_idx = user_data['current_question']
    if current_idx >= len(user_data['questions']):
        bot.answer_callback_query(call.id, "Тест завершен.")
        return

    question_data = user_data['questions'][current_idx]
    correct_answers = question_data[1][0]
    user_answer = call.data

    if user_answer in correct_answers:
        user_data['correct'] += 1

    user_data['current_question'] += 1
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.answer_callback_query(call.id)
    send_question(user_id)


def calculate_result(user_id):
    user_data = user_states.pop(user_id, None)
    if not user_data:
        return

    total = len(user_data['questions'])
    correct = user_data['correct']
    progress = (correct / total) * 100

    if progress >= 80:
        level = "B1"
    elif progress >= 60:
        level = "A2"
    else:
        level = "A1"

    bot.send_message(user_id, f"🏆 Результат теста:\nУровень: {level}\nПравильных ответов: {correct}/{total}")



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
if __name__ == "__main__":
    bot.polling(none_stop=True)