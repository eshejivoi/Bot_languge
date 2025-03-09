import random
import speech_recognition as sr
from googletrans import Translator

def translate_text(text, dest_lang):
    translator = Translator()
    translated = translator.translate(text, dest=dest_lang)
    return translated.text

# Функция для получения вопроса и вариантов для теста
def get_test_question(level):
    questions = test_questions.get(level, [])
    question, options = random.choice(questions)
    return question, options

# Функция для проверки ответа (с несколькими правильными ответами)
def check_answer(user_answer, correct_answers):
    return user_answer in correct_answers

# Прогресс пользователя: сохранение его результатов
def track_progress(user_data, correct_answers, total_questions):
    # Считаем правильные ответы и вычисляем процент
    correct = sum(1 for answer in user_data if answer in correct_answers)
    progress = (correct / total_questions) * 100
    return progress

# Функция для преобразования голосового сообщения в текст
def recognize_speech(audio_file_path):
    recognizer = sr.Recognizer()

    # Открываем аудиофайл
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)  # Считываем весь файл в память

    try:
        # Используем Google Web Speech API для распознавания речи
        recognized_text = recognizer.recognize_google(audio)
        return recognized_text
    except sr.UnknownValueError:
        return "Ошибка, не удалось распознать речь"
    except sr.RequestError:
        return "Ошибка с интернет-соединением"

# Функция для проверки произнесенной фразы
def check_pronunciation(user_audio_text, correct_phrase):
    return user_audio_text.strip().lower() == correct_phrase.strip().lower()


