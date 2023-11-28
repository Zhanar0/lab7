# Напишите программу для подсчета частоты слов в файле

def word_frequency(file_name):
    try:
        with open(file_name, 'r') as file:
            # считываем содержимое и преобразуем к нижнему регистру
            content = file.read().lower()
            words = content.split()  # разбиваем содержимое на слова

            word_count = {}
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

            # выводим частоту слов
            for word, count in word_count.items():
                print(f"'{word}': {count}")
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")


# Вызываем функцию, передавая имя файла
word_frequency("text1.txt")
