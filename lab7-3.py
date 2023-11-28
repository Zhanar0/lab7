# Напишите функцию для подсчета символов верхнего регистра в текстовом файле

def count_characters(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            uppercase_count = sum(1 for char in content if char.isupper())
            print(f"Количество символов верхнего регистра в файле: {uppercase_count}")
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")


# вызоваем функцию, передав имя файла
count_characters("text1.txt")
