import random

# Список вопросов для теста
test_questions = {
    "A1": [
        ("What's your name?", ["My name is John", "I am from London", "Hello"]),
        ("How old are you?", ["I'm 20", "I am happy", "I like music"]),
        ("Where are you from?", ["I am from Paris", "I like reading", "My name is Anna"]),
    ],
    "A2": [
        ("What do you do?", ["I'm a teacher", "I like swimming", "My favorite color is blue"]),
        ("Can you speak English?", ["Yes, I can", "I am a student", "It's raining"]),
        ("What did you do yesterday?", ["I went to the cinema", "I am going to work", "I like pizza"]),
    ],
    "B1": [
        ("What are your plans for the weekend?", ["I will visit my friend", "I like ice cream", "I'm reading a book"]),
        ("Tell me about your last vacation.", ["I went to Spain last summer", "I am going to the market", "My favorite hobby is painting"]),
        ("What do you think about global warming?", ["It's a big problem", "I have a dog", "I like sports"]),
    ]
}

# Функция для получения вопроса и вариантов для теста
def get_test_question(level):
    questions = test_questions.get(level, [])
    question, options = random.choice(questions)
    return question, options

# Функция для проверки ответа
def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer
