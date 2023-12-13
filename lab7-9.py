# Напишите функцию, которая отображала бы исправленную версию всего содержимого файла,
#все символы «B» будут отображатьсякак символ «J»
# Определение функции для замены символов в текстовом файле
def replace_char(file_name, old_char, new_char):
    try:
         # Открытие файла для чтения ('r') с использованием контекстного менеджера 'with open'
        with open(file_name, 'r') as file:
            # проходимся по содержимому файла
            content = file.read()

            # изменяем старые буквы на новые в содержимом
            correct_content = content.replace(old_char, new_char)

            # выводим новое содержание
            print(correct_content)
    except FileNotFoundError:
        print(f"File {file_name} not found.")


# вызываем функцию, передав имя файла и символы для замены
replace_char("text1.txt", "B", "J")
