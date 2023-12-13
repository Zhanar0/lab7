# Напишите функцию для подсчета слов «all» и «none», присутствующих в текстовом файле.
# [Обратите внимание, что слова «all» и «none» являются полными словами]

def all_and_none(text1.txt):


try:
 # Открытие файла для чтения ('r'),'with open'- контекстный менеджер,котрый обеспечивает выполнение операций "входа" и "выхода" тем самым упрощает управление работы с файлами 
    with open(text1.txt, 'r') as file:
         # Чтение всего содержимого файла и сохранение его в переменной content
        content = file.read()
        # [content.split() ]разделяет содержимое на слова.
        words = content.split()  # Split the content into words
         # Используем метод count() для подсчета вхождений слов 'all' и 'none'.
        count_all = words.count("all")
        count_none = words.count("none")
        # Вывод результатов подсчета на экран
        print(f"Count of 'all': {count_all}")
        print(f"Count of 'none': {count_none}")
except FileNotFoundError:
     # Обработка исключения, если файл не найден
    print(f"File {file_name} not found.")

# вызываем функцию
all_and_none("text1.txt")
