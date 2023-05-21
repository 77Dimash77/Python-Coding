# Задача 34:  Винни-Пух попросил Вас посмотреть, 
# есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, 
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке

def check_rhythm(poem):
    lines = poem.split()
    first_line_syllables = count_syllables(lines[0])
    for line in lines:
        syllables = count_syllables(line)
        if syllables != first_line_syllables:
            return "Пам парам"
    return "Парам пам-пам"
def count_syllables(phrase):
    vowels = "аеёиоуыэюя"
    syllables = 0
    for word in phrase.split('-'):
        for char in word:
            if char.lower() in vowels:
                syllables += 1
    return syllables
poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)