# Запрашиваем у пользователя строку на русском языке
input_string = input("Введите строку на русском языке: ")

# Инициализация переменных для хранения количества гласных и согласных
vowels = 0
consonants = 0

# Множества гласных и согласных букв на русском языке
vowel_set = set("аеёиоуыэюяАЕЁИОУЫЭЮЯ")
consonant_set = set("бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ")

# Подсчёт длины строки
length = 0
for char in input_string:
    length += 1

# Подсчёт гласных и согласных
for char in input_string:
    if char in vowel_set:
        vowels += 1
    elif char in consonant_set:
        consonants += 1

# Вывод результатов
print("Длина строки:", length)
print("Количество гласных:", vowels)
print("Количество согласных:", consonants)
