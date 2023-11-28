# Напишите программу для поиска самого длинного слова в текстовом файле


def longest_word(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read().lower()  # считываем содержимое и преобразуем к нижнему регистру
            words = content.split()  # разбиваем содержимое на слова

            longest_word = max(words, key=len)  # находим самое длинное слово с помощью max

            print(f"The longest word in the file is: '{longest_word}'")
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")


# вызываеи функцию, передавая имя файла
longest_word("text1.txt")
