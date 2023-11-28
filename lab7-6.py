# Напишите функцию для подсчета слов «all» и «none», присутствующих в текстовом файле.
# [Обратите внимание, что слова «all» и «none» являются полными словами]

def all_and_none(text1.txt):


try:
    with open(text1.txt, 'r') as file:
        content = file.read()
        words = content.split()  # Split the content into words
        count_all = words.count("all")
        count_none = words.count("none")
        print(f"Count of 'all': {count_all}")
        print(f"Count of 'none': {count_none}")
except FileNotFoundError:
    print(f"File {file_name} not found.")

# вызываем функцию
all_and_none("text1.txt")
