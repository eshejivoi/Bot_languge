import random
import speech_recognition as sr
from googletrans import Translator

def translate_text(text, dest_lang):
    translator = Translator()
    translated = translator.translate(text, dest=dest_lang)
    return translated.text


test_questions = {
    "A1": [
        ("What's your name?", [["My name is John", "I am from London"], "Hello"]),
        ("How old are you?", [["I'm 20", "I'm 25"], "I like music"]),
        ("Where are you from?", [["I am from Paris", "I am from Italy"], "I like reading"]),
        ("What time is it?", [["It’s 3 o’clock", "It’s 5 o’clock"], "It’s raining"]),
        ("What is your favorite color?", [["My favorite color is blue", "I like red"], "I am a teacher"]),
        ("Do you like sports?", [["Yes, I like football", "Yes, I like tennis"], "I am 30 years old"]),
        ("Can you speak English?", [["Yes, I can", "I am learning English"], "I like ice cream"]),
        ("How are you?", [["I am fine, thank you", "I’m good, thanks"], "It’s 10 o’clock"]),
        ("What’s the weather like?", [["It’s sunny", "It’s hot"], "I’m hungry"]),
        ("What do you do?", [["I am a student", "I am a teacher"], "I like pizza"]),
    ],

    "A2": [
        ("What do you do in your free time?", [["I like playing basketball", "I like swimming"], "I am busy"]),
        ("Can you play the guitar?", [["Yes, I can play the guitar", "Yes, I play piano"], "I like sports"]),
        ("Where do you live?", [["I live in London", "I live in New York"], "I like reading books"]),
        ("How often do you go to the gym?", [["I go three times a week", "I go once a week"], "I’m cooking dinner"]),
        ("What did you do last weekend?", [["I visited my grandparents", "I went hiking"], "I am studying English"]),
        ("Do you like watching movies?", [["Yes, I love watching movies", "I like documentaries"], "I like to read books"]),
        ("Can you cook?", [["Yes, I can cook pasta", "Yes, I can make a sandwich"], "I am learning English"]),
        ("What’s your favorite food?", [["My favorite food is pizza", "I like sushi"], "I like swimming"]),
        ("How do you get to work?", [["I take the bus", "I walk to work"], "I have a cat"]),
        ("Where is your favorite place?", [["My favorite place is the beach", "I like the mountains"], "I like music"]),
    ],

    "B1": [
        ("What do you think about social media?", [["I think social media is useful", "It’s a good way to communicate"], "I like playing chess"]),
        ("How do you usually spend your holidays?", [["I usually visit new countries", "I go to the beach"], "I enjoy hiking"]),
        ("Can you describe your hometown?", [["My hometown is small and peaceful", "I love my hometown"], "I like reading"]),
        ("What are your career goals?", [["I want to become a software engineer", "I want to work as a doctor"], "I like traveling"]),
        ("Do you prefer reading books or watching movies?", [["I prefer reading books", "I like both reading books and watching movies"], "I am going to work"]),
        ("How important is education to you?", [["Education is very important to me", "I think education is the key to success"], "I like to read novels"]),
        ("Tell me about your last trip.", [["I went to Spain last summer", "I visited Italy last year"], "I like sports"]),
        ("How would you improve the environment?", [["I would reduce plastic use", "I would promote recycling"], "I am going to the beach"]),
        ("What’s your opinion on global warming?", [["It’s a serious problem", "It’s something we should address"], "I like swimming"]),
        ("What would you do if you won the lottery?", [["I would travel around the world", "I would donate to charity"], "I like singing"]),
    ]
}

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

