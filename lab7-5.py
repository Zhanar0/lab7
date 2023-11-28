# Напишите функцию для подсчета слов в текстовом файле,
# оканчивающихся на букву «F» (включая небольшие регистры)

# Модуль re (регулярные выражения) в Python  позволяют искать, заменять и делить текст на основе паттернов,шаблонов.
# Функция re.findall() возвращает все непересекающиеся совпадения шаблона в строке в виде списка


import re


def words_ending_with_F(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            words = re.findall(r'\b\w*F\b', content, re.IGNORECASE)
            count = len(words)
            print(f"Количество слов, оканчивающихся на 'F': {count}")
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")


# вызываем функцию, передав имя файла
count_words_ending_with_F("text1.txt")
