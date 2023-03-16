#  #  Нахождение площади треугольника
# a = float(input())
# b = float(input())
# square = 0.5 * a * b
# print(square)

#  #  Нахождение времени до встречи двух объектов
# s = float(input())
# v1 = float(input())
# v2 = float(input())
# t = s / (v1 + v2)
# print(t)

#  #  Нахождение обратного числа
# number = float(input())
# if number != 0:
#     print(number ** -1)
# else:
#     print('Обратного числа не существует')

#  #  Конвертация температуры из Фаренгейт в Цельсий
# fahrengheit = float(input())
# celsium = (5/9)*(fahrengheit - 32)
# print(celsium)

#  #  Программа, которая вычисляет возраст собаки в человеческих годах
# dog_age = int(input())
# if 0 < dog_age < 3:
#     print(dog_age * 10.5)
# else:
#     print(21 + (dog_age - 2) * 4)

#  #  Вывести первую цифру после запятой
# number = float(input())
# first_number = number * 10 % 10
# first_number = int(first_number)
# print(first_number)

#  #  Вывод его дробной части
# number = float(input())
# last_numbers = ((number * 10) % 10) / 10
# print(last_numbers)

#  #  Программa, которая находит наименьшее и наибольшее из пяти чисел
# a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(
#     input())
# minimal_number = min(a, b, c, d, e)
# maximal_number = max(a, b, c, d, e)
# print('Наименьшее число =', minimal_number)
# print('Наибольшее число =', maximal_number)

#  #  Программa, которая упорядочивает три числа от большего к меньшему
# a, b, c = int(input()), int(input()), int(input())
# maximal = max(a, b, c)
# minimal = min(a, b, c)
# print(maximal)
# print((a + b + c) - (maximal + minimal))
# print(minimal)

# # Нахождение "интересного числа"
# number = int(input())
# a = number // 100
# b = number // 10 % 10
# c = number % 10
# maximal = max(a, c, b)
# minimal = min(a, c, b)
# if maximal - minimal == ((a + b + c) - (maximal + minimal)):
#     print('Число интересное')
# else:
#     print('Число неинтересное')

# #  Программа вычисляющая сумму модулей 5-ти чисел
# a = float(input())
# b = float(input())
# c = float(input())
# d = float(input())
# e = float(input())
# print(abs(a) + abs(b) + abs(c) + abs(d) + abs(e))

# #  Программа определяющая манхэттенское расстояние между двумя точками, координаты которых заданы
# p1 = int(input())
# p2 = int(input())
# q1 = int(input())
# q2 = int(input())
# print(abs(p1-q1) + abs(p2-q2))
