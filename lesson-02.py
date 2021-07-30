## -*- coding: utf-8 -*-
# -*- coding: ascii -*-
# ДЗ 2


print('Задание № 01')
#1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
while True:
    first_value = input('Введите первый операнд (используйте знак "." для разделения целой и дробной части): ').lstrip().rstrip()
    if not first_value.replace('.', '').replace(',', '').isdigit():
        raise ValueError
    first_value = float(first_value.replace(',', '.'))
    operation = '#'
    while operation not in ['0', '+', '-', '*', '/', '^', '%']:
        operation = input('Введите операцию: (0 - выход, +, -, *, /, ^, //, %): ').lstrip().rstrip()
        if operation not in ['0', '+', '-', '*', '/', '^', '%']:
            print('Знак [{}] операции вне допустимого диапазона [{}].'.format(operation, '0, +, -, *, /, ^, //, %'))
    if operation == '0':
        break

    second_value = input('Введите второй операнд (используйте знак "." для разделения целой и дробной части): ').lstrip().rstrip()
    if not second_value.replace('.', '').replace(',', '').isdigit():
        raise ValueError
    second_value = float(second_value.replace(',', '.'))

    if operation in ['/', '//'] and second_value == 0.0:
        print('Деление на ноль!')
    else:
        op = str(first_value) + ' ' + operation + ' ' + str(second_value)
        print('{} = {}'.format(op, eval(op)))

print('Задание № 02')
#2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
value = input('Введите число (используйте знак "." для разделения целой и дробной части): ').lstrip().rstrip()
even_count, odd_count = 0, 0
for el in value:
    if el.isdigit():
        if int(el) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
print('Число {} содержит: четных - {}, не четных - {} цифр.'.format(value, even_count, odd_count))

print('Задание № 03')
#3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
int_value = input('Введите целое число: ').lstrip().rstrip()
if not int_value.isdigit():
    raise ValueError
print(int_value[::-1])

print('Задание № 04')
#4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
n = input('Введите колличество элементов ряда: ').lstrip().rstrip()
if not n.isdigit():
    raise ValueError
else:
    n = int(n)
row = [1, ]
for i in range(1, n+1):
    el = row[i-1]/-2
    row.append(el)
print('Последовательность:', row)
print('Сумма элементов:', sum(row))

print('Задание № 05')
#5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
from itertools import islice
cells = (f"{i:x} {chr(i):<4}" for i in range(32, 127))
for _ in range(32, 127, 10):
    print(*islice(cells, 0, 10))

print('Задание № 06')
#6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
import random as rnd
magic_value = 56 #rnd.randint(0, 100)
try_cnt = 1
while try_cnt <= 10:
    user_value = int(input('Введите целое число от 0 до 100, попытка [{} из {}]: '.format(try_cnt, 10)).lstrip().rstrip())
    user_result = 1 if user_value == magic_value else (0.5 if user_value < magic_value else 1.5)
    print(user_result)
    if user_result == 1:
        print('Поздравляю - число {} угадано за {} попыток!!!'.format(magic_value, try_cnt))
        break
    print('Загаданное число {} введенного Вами.'.format(('БОЛЬШЕ' if user_result == 0.5 else 'МЕНЬШЕ')))
    try_cnt += 1

print('Задание № 07')
#7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n - любое натуральное число.
n = input('Введите натуральное: ').lstrip().rstrip()
if not n.replace('.', '').replace(',', '').isdigit():
    raise ValueError
n = int(n.replace(',', '.'))
print(*range(1, n+1))
s = sum(range(1, n+1))
print('Сумма:', s)
print('n(n+1)/2 =', (n*(n+1))/2)

print('Задание № 08')
#8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
sRange = input('Введите последовательность чисел (через пробел): ')
sToSearch = input('Введите цифру для поиска и подсчета: ')
if not sToSearch.replace('.', '').replace(',', '').isdigit():
    raise ValueError
print('Цифра {} встретилась {} раз в веденной последовательности.'.format(sToSearch, sRange.count(sToSearch)))


print('Задание № 09')
#9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

def dSum(elements):
    return sum([int(x) for x in elements])

sRange = input('Введите последовательность чисел (через пробел): ')
lRange = sRange.split()
sRange = [dSum(i) for i in lRange]

print('Число {} с максимальной суммой цифр равной {}'.format(lRange[sRange.index(max(sRange))], max(sRange)))
