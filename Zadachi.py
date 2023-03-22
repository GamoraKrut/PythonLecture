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

# # Программа, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу
# firstname = input()
# lastname = input()
# print('Hello ' + firstname + ' ' + lastname +
#       '! ' + 'You just delved into Python')

# # Программа, которая считывает с клавиатуры название футбольной команды и выводит фразу:
#  #«Футбольная команда [введённая строка] имеет длину [длина введённой строки] символов».
# team = input()
# print('Футбольная команда ' + team +
#       ' имеет длину ' + str(len(team)) + ' символов')

# # Программа, которая определяет самое короткое и самое длинное название города
# first = str(input())
# second = str(input())
# third = str(input())
# maximal = max(len(first), len(second), len(third))
# minimal = min(len(first), len(second), len(third))
# if minimal == len(first):
#     print(first)
# elif minimal == len(second):
#     print(second)
# elif minimal == len(third):
#     print(third)
# if maximal == len(first):
#     print(first)
# elif maximal == len(second):
#     print(second)
# elif maximal == len(third):
#     print(third)

# # Вводятся 3 строки в случайном порядке. Напишите программу,
# # которая выясняет можно ли из длин этих строк построить
# # возрастающую арифметическую прогрессию.
# i, j, k = str(input()), str(input()), str(input())
# i = len(i)
# j = len(j)
# k = len(k)
# if (2 * i - j - k) * (2 * j - i - k) * (2 * k - i - j) == 0:
#     print('YES')
# else:
#     print('NO')

# # Программу, которая считывает одну строку,
# # после чего выводит «YES», если в введенной
# # строке есть подстрока «синий» и «NO» в противном случае
# string = str(input())
# if 'синий' in string:
#     print('YES')
# else:
#     print('NO')

# # Программа определяющая евклидово расстояние между двумя точками, координаты которых заданы.
# from math import *
# x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
# p = sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
# print(p)

# # Программа определяющая площадь круга и длину окружности по заданному радиусу R
# from math import pi
# r = float(input())
# s = pi * pow(r, 2)
# c = 2 * pi * r
# print(s)
# print(c)

# # Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное
# from math import *
# a, b = float(input()), float(input())
# mid_ariph = (a + b) / 2
# mid_geom = sqrt((a * b))
# mid_garmon = (2 * (a * b)) / (a + b)
# mid_sqare = sqrt((pow(a, 2) + pow(b, 2)) / 2)
# print(mid_ariph)
# print(mid_geom)
# print(mid_garmon)
# print(mid_sqare)

# # Даны три вещественных числа a, b, c. Программа, которая находит вещественные корни квадратного уравнения
# # a * (x ** 2) + bx + c == 0
# from math import *
# a, b, c = float(input()), float(input()), float(input()),
# d = pow(b, 2) - (4 * a * c)
# if d < 0:
#     print('Нет корней')
# elif d == 0:
#     print(- b / (2 * a))
# else:
#     x1 = (- b + sqrt(d)) / (2 * a)
#     x2 = (- b - sqrt(d)) / (2 * a)
#     minimal = min(x1, x2)
#     maximal = max(x1, x2)
#     print(minimal)
#     print(maximal)
