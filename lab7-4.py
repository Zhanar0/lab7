# Напишите функцию для подсчета символов верхнего регистра в текстовом файле

def not_starting_with_D(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            count = sum(1 for line in lines if not line.strip().startswith('D'))
            print(f"Вывод: {count}")
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")


# вызываем функцию, передав имя файла
not_starting_with_D("text1.txt")
