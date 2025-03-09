import telebot
from config import TOKEN
from logic import test_questions
import random

bot = telebot.TeleBot(TOKEN)
user_states = {}


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


if __name__ == "__main__":
    bot.polling(none_stop=True)