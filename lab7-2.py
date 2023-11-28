#Напишите программу для чтения случайной строки из файла.
import random


def random_line_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            if lines:
                random_line = random.choice(lines)
                print("Random Line: ", random_line, end='')
            else:
                print("The file is empty.")
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")


# вызываем функцию  передавая имя файла
random_line_file("text1.txt")
