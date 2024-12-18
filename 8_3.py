def get_number(num):
    while True:
        try:
            user_input = input(num)
        except ValueError:
            print("Ошибка: пожалуйста, введите только числа, разделённые пробелами.")
        else:
            number_set = set(map(float, user_input.split()))
            return number_set


set1 = get_number("Введите первый набор чисел (через пробел): ")
set2 = get_number("Введите второй набор чисел (через пробел): ")

# Находим пересечение двух множеств (работает только с мн-и)
peresechenie = set1.intersection(set2)

if peresechenie:
    print("Числа, которые встречаются в обоих наборах:")
    print(peresechenie)
else:
    print("Нет чисел, которые встречаются в обоих наборах.")
