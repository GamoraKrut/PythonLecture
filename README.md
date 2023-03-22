# PythonLecture

* *print(sep='@')* - **sep**- заменяет пробел на символ

* *print(end='@')* - **end**- ставит в конце вывода символ; /n после end переводит строку

# Операции с числами

** - возведение в степень

% - остаток от деления

// - целочисленное деление

* _total_ - a + b

* _diff_ - a - b

* _prod_ - a * b

* div1 = a / b

* div2 = a // b *Целочисленное деление*

* mod = a % b *Деление с остатком*

* exp = a ** b *возведение числа __a__ в степень __b__*

*Пример:*

```python
print(a, '+', b, '=', total)
print(a, '-', b, '=', diff)
print(a, '*', b, '=', prod)
print(a, '/', b, '=', div1)
print(a, '//', b, '=', div2)
print(a, '%', b, '=', mod)
print(a, '**', b, '=', exp)
```
*На выводе будет:*
```python
13 + 7 = 20
13 - 7 = 6
13 * 7 = 91
13 / 7 = 1.8571428571428572
13 // 7 = 1
13 % 7 = 6
13 ** 7 = 62748517
```

## Оффтоп:

Для удобного чтения чисел можно использовать символ подчеркивания:

```python
num1 = 25_000_000
num2 = 25000000
print(num1)
print(num2)
```
Результатом выполнения такого кода будет:
```python
25000000
25000000
```

# Операции со строками:

* ## Канкатенация - сложение строк

Пример: 

```python
s1 = 'ab' + 'bc'
s2 = 'bc' + 'ab'
s3 = s1 + s2 + '!!'
print(s1)
print(s2)
print(s3)
```

Результат:
```Python
abbc
bcab
abbcbcab!!
```

* ## Умножение

Пример:
```Python
s = 'Hi' * 4
print(s)
```
```python
HiHiHiHi
```

* Тройные кавычки '''...''' можно использовать для многострочного текста

Пример:

```Python
text = '''Python is an interpreted, high-level, general-purpose programming language.
Created by Guido van Rossum and first released in 1991, Python design 
philosophy emphasizes code readability with its notable use of significant whitespace.'''
print(text)
```

На выводе будет:

```
Python is an interpreted, high-level, general-purpose programming language.
Created by Guido van Rossum and first released in 1991, Python design 
philosophy emphasizes code readability with its notable use of significant whitespace.
```

* ## Оператор __*in*__ - c его помощью можно можно проверить находится ли одна строка внутри другой

Пример:

```python
s = input()
if 'a' in s:
    print('Введенная строка содержит символ а')
else:
    print('Введенная строка не содержит символ а')
```

* **Примечание**
 Если строка s1 содержится в строке s2, то говорят, что строка s1 является подстрокой для строки s2. Другими словами, оператор in определяет является ли одна строка подстрокой другой.

# Функции
* ## *__min__* - находит самое маленькое значение в списке

* ## *__max__* - находит самое большое значение в списке

* ## *__abs__* - находитмодуль числа

Примеры:

Pезультатом выполнения следующего кода:
```python
a = max(3, 8, -3, 12, 9)
b = min(3, 8, -3, 12, 9)
c = max(3.14, 2.17, 9.8)
print(a)
print(b)
print(c)
```

будет:

```python
12
-3
9.8
```

Pезультатом выполнения следующего кода

```python
print(abs(10))
print(abs(-7))
print(abs(0))
print(abs(-17.67))
```

будет:

```python
10
7
0
17.67
```

* ## *len( )* - Считает длинну строки

Пример:
```python
s1 = 'abcdef'
length1 = len(s1)               # считаем длину строки из переменной s1
length2 = len('Python rocks!')  # считаем длину строкового литерала
print(length1)
print(length2)
```

Вывод:

```python
6
13
```

