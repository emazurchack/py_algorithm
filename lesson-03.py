# -*- coding: utf-8 -*-

"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
4. Определить, какое число в массиве встречается чаще всего.
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

print('Задание № 01')
print({el: len([*range(el, 100, el)]) for el in range(2, 10)})
print('Задание № 02')
elements = [8, 3, 15, 6, 4, 2]
print([idx for idx, el in enumerate(elements) if el % 2 == 0])
print('Задание № 03')
lst = [1, 8, 4, 5, 2, 9, 1, 0]
print('before: ', lst)
lst[lst.index(min(lst))], lst[lst.index(max(lst))] = lst[lst.index(max(lst))], lst[lst.index(min(lst))]
print('after: ', lst)
print('Задание № 04')
lst = [1, 3, 4, 5, 3, 6, 7, 2, 3, 1, 8, 4, 9, 1, 1]
cnt_lst = [lst.count(i) for i in lst]
#print(lst)
print(f'элемент [{lst[cnt_lst.index(max(cnt_lst))]}] встречается {cnt_lst[cnt_lst.index(max(cnt_lst))]} раз(а).')
print('Задание № 05')
lst = [1, -3, 4, 5, 3, 6, 4, 7, -7, 2, 3, 1, 8, 4, -9, 1, -1]
mx = max([i for i in lst if i < 0])
print(f'Макс. отрицат. элемент [{mx}], позиция в массиве [{lst.index(mx)}]')
print('Задание № 06')
lst = [1, -3, 4, 5, 3, 6, 4, 7, -7, 2, 3, 1, 8, 4, 5, -9, 1, -1]
max_el, min_el = max(lst), min(lst)
if min(lst.index(max_el), lst.index(min_el))+1 == max(lst.index(max_el), lst.index(min_el)):
    print(lst[min(lst.index(max_el), lst.index(min_el))+1])
else:
    print(sum(lst[min(lst.index(max_el), lst.index(min_el))+1: max(lst.index(max_el), lst.index(min_el))]))
print('Задание № 07')
from random import randint
rnd_lst = [randint(-20, 20) for _ in range(10)]
print(rnd_lst)
min_el1, min_idx1 = min(rnd_lst), rnd_lst.index(min(rnd_lst))
lst = [el for idx, el in enumerate(rnd_lst) if idx != min_idx1]
min_el2, min_idx2 = min(lst), lst.index(min(lst))
print(f'min elements: {min_el1}, {min_el2}')
print('Задание № 08')

rows, cols = 5, 4
mx = []
for i in range(rows):
    row = list(map(int, input(f'введите {cols} элементов строки {i}, через пробел').strip().split()))
    row.append(sum(row))
    mx.append(row)
print(mx)

print('Задание № 09')
lst = [[randint(-10, 10) for _ in range(10)] for _ in range(10)]
mins = [sum(r) for r in zip(*lst)]
print(f'Min of cols: {mins}')
print(f'MAX element in minimums of cols: {max(mins)}')

