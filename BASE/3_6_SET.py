"""
Модуль 3.6 "Множества"
"""

"""
Задача 1.
Даны два списка студентов, посещавших два разных курса.
Найдите студентов, которые посещали оба курса.
"""

python_course = ["Анна", "Борис", "Виктор", "Галина", "Дмитрий"]
java_course = ["Борис", "Галина", "Елена", "Жанна", "Захар"]

result = set(python_course + java_course)
print(f'----- Задача 1:\n {result}')

"""
Задача 2.
Дана строка. 
Определите, сколько в ней уникальных символов (без учёта пробелов).
"""

text = "программирование это интересно"

print(f'----- Задача 2: \n {len(set(text)) - 1} символов.')

"""
Задача 3.
Даны три множества. 
Найдите элементы, которые встречаются ровно в двух множествах из трёх.
"""

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = {1, 5, 8, 9, 10}

all_elements = a.union(b, c)

some_dict = {}

for element in all_elements:
    if element in a and element in b:
        some_dict[element] = 'a, b'
    elif element in b and element in c:
        some_dict[element] = 'b, c'

print('----- Задача 3:')
for element in some_dict:
    print(f'Элемент: {element}'
          f' содержится в множествах: {some_dict[element]}')
else:
    print('Остальные элементы уникальны.')

"""
Задача 4.
Напишите программу, 
которая проверяет, является ли одно слово анаграммой другого. 
Анаграмма — это слово, составленное из тех же букв (например, "кот" и "ток").
"""

test_elements_dict = {
    # Базовые анаграммы
    "кот": "ток",
    "питон": "топин",
    "привет": "пока"
}


def is_anagram(word1, word2):
    word1 = word1.lower().replace(' ', '')
    word2 = word2.lower().replace(' ', '')
    if len(word1) != len(word2):
        return False
    elif (not word1.isalpha() or
          not word2.isalpha()):
        return False
    else:
        return sorted(word1) == sorted(word2)


print('----- Задание 4:')

for element_1, element_2 in test_elements_dict.items():
    if is_anagram(element_1, element_2):
        print(f'Пара: {element_1}, {element_2} - [✓] анаграмма')
    else:
        print(f'Пара: {element_1}, {element_2} - [x] не анаграмма')

"""
Задача 5.
Дан список слов. Создайте словарь, где ключ — frozenset букв слова, 
а значение — список всех слов с таким набором букв.
"""

words = ["кот", "ток", "окт", "дом", "мод", "питон", "топин", "слово"]

some_dict_2 = {}

for word in words:
    key = frozenset(word)
    if key not in some_dict_2:
        some_dict_2[key] = []
    some_dict_2[key].append(word)

print('----- Задача 5:')

for key, value in some_dict_2.items():
    print(f'Ключ: {key} \n'
          f'Значения: {value}')
