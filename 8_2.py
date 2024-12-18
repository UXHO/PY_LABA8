str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")

# Преобразуем строки в множества символов
set1 = set(str1)
set2 = set(str2)

# Символы, которые есть в первой строке, но нет во второй
unique_chars = set1 - set2
if unique_chars:
    print("Символы, которые есть в первой строке, но не во второй:")
    print(unique_chars)
else:
    print("Нет символов, которые есть в первой строке, но не во второй.")
    