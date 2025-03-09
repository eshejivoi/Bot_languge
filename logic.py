import random


test_questions = {
    "A1": [
        ("What's your name?", ["My name is John", "I am from London", "Hello"]),
        ("How old are you?", ["I'm 20", "I am happy", "I like music"]),
        ("Where are you from?", ["I am from Paris", "I like reading", "My name is Anna"]),
        ("What time is it?", ["It’s 3 o’clock", "It’s raining", "I’m tired"]),
        ("What is your favorite color?", ["My favorite color is blue", "I am a teacher", "I am from Spain"]),
        ("Do you like sports?", ["Yes, I like football", "I am 30 years old", "I am reading a book"]),
        ("Can you speak English?", ["Yes, I can", "I am going to school", "I like ice cream"]),
        ("How are you?", ["I am fine, thank you", "I’m a doctor", "It’s 10 o’clock"]),
        ("What’s the weather like?", ["It’s sunny", "I am going to the park", "I’m hungry"]),
        ("What do you do?", ["I am a student", "I am from Italy", "I like pizza"]),
    ],
    
    "A2": [
        ("What do you do in your free time?", ["I like playing basketball", "I am going to work", "I am busy"]),
        ("Can you play the guitar?", ["Yes, I can play the guitar", "I like sports", "It’s a beautiful day"]),
        ("Where do you live?", ["I live in London", "I am 25 years old", "I like reading books"]),
        ("How often do you go to the gym?", ["I go three times a week", "I like swimming", "I’m cooking dinner"]),
        ("What did you do last weekend?", ["I visited my grandparents", "I work in an office", "I am studying English"]),
        ("Do you like watching movies?", ["Yes, I love watching movies", "I like to read books", "I play football"]),
        ("Can you cook?", ["Yes, I can cook pasta", "I like pizza", "I am learning English"]),
        ("What’s your favorite food?", ["My favorite food is pizza", "I like swimming", "I am studying"]),
        ("How do you get to work?", ["I take the bus", "I like running", "I have a cat"]),
        ("Where is your favorite place?", ["My favorite place is the beach", "I go to work", "I like music"]),
    ],
    
    "B1": [
        ("What do you think about social media?", ["I think social media is useful", "I like playing chess", "It’s rainy"]),
        ("How do you usually spend your holidays?", ["I usually visit new countries", "I like to play football", "I enjoy hiking"]),
        ("Can you describe your hometown?", ["My hometown is small and peaceful", "I work in an office", "I like reading"]),
        ("What are your career goals?", ["I want to become a software engineer", "I like traveling", "I study English"]),
        ("Do you prefer reading books or watching movies?", ["I prefer reading books", "I like watching TV", "I am going to work"]),
        ("How important is education to you?", ["Education is very important to me", "I like to read novels", "I am learning math"]),
        ("Tell me about your last trip.", ["I went to Spain last summer", "I like sports", "I am traveling"]),
        ("How would you improve the environment?", ["I would reduce plastic use", "I like ice cream", "I am going to the beach"]),
        ("What’s your opinion on global warming?", ["It’s a serious problem", "I like swimming", "I work in an office"]),
        ("What would you do if you won the lottery?", ["I would travel around the world", "I am studying", "I like singing"]),
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
