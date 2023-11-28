#Напишите функцию для чтения содержимого текстового файла «text1.txt»
# построчно и отображения его на экране

def r_d_file(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")

#вызываем функцию, передавая ей имя файла "text1.txt"
r_d_file("text1.txt")
