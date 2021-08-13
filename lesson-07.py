# -*- coding: utf-8 -*-
"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
    Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
    По возможности доработайте алгоритм (сделайте его умнее).
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
    Выведите на экран исходный и отсортированный массивы.
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
    Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
    Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
"""
from random import randint, choice
print('Задание № 01')

def bubbleSort(array_to_sort):
    for i in range(len(array_to_sort)):
        for j in range(0, len(array_to_sort) - i - 1):
            if array_to_sort[j] < array_to_sort[j + 1]:
                array_to_sort[j], array_to_sort[j + 1] = array_to_sort[j + 1], array_to_sort[j]

a = [randint(-100, 100) for _ in range(30)]
print('before Bubble sort: ', a)
bubbleSort(a)
print('after Bubble sort:', a)

def bubbleSortMod(array_to_sort):
	changed = True
	while changed:
		changed = False
		for i in range(len(array_to_sort) - 1):
			if array_to_sort[i] < array_to_sort[i+1]:
				array_to_sort[i], array_to_sort[i+1] = array_to_sort[i+1], array_to_sort[i]
				changed = True

aa = [randint(-100, 100) for _ in range(30)]
print('before Bubble MOD sort: ', aa)
bubbleSortMod(aa)
print('after Bubble MOD sort:', aa)

print('Задание № 02')
def merge(a, lb, split, ub):
    # Слияние упорядоченных частей массива в буфер temp
    # с дальнейшим переносом содержимого temp в a[lb]...a[ub]
    pos1 = lb # текущая позиция чтения из первой последовательности a[lb]...a[split]
    pos2 = split + 1 # текущая позиция чтения из второй последовательности a[split+1]...a[ub]
    pos3 = 0 # текущая позиция записи в temp
    temp = [i for i in range(ub - lb + 1)]
    # идет слияние, пока есть хоть один элемент в каждой последовательности
    while pos1 <= split and pos2 <= ub:
        if a[pos1] < a[pos2]:
            temp[pos3] = a[pos1]
            pos1 += 1
            pos3 += 1
        else:
            temp[pos3] = a[pos2]
            pos2 += 1
            pos3 += 1
    # одна последовательность закончилась - копировать остаток другой в конец буфера
    while pos2 <= ub:  # пока вторая последовательность непуста
        temp[pos3] = a[pos2]
        pos3 += 1
        pos2 += 1
    while pos1 <= split:  # пока первая последовательность непуста
        temp[pos3] = a[pos1]
        pos3 += 1
        pos1 += 1

    a[lb:ub + 1] = temp # скопировать буфер temp в a[lb]...a[ub]
    del(temp)

def mergeSort(a, lb=0, ub=-1):
    if lb < ub:  # если есть более 1 элемента
        split = (lb + ub) // 2          # индекс, по которому делим массив
        mergeSort(a, lb, split)         # сортировать левую половину
        mergeSort(a, split + 1, ub)     # сортировать правую половину
        merge(a, lb, split, ub)         # слить результаты в общий массив

aaa = [randint(-100, 100) for _ in range(30)]
print('before Merge sort: ', aaa)
mergeSort(aaa, 0, len(aaa)-1)
print('after Merge sort:', aaa)

print('Задание № 03')
def quick_select(l, k, pivot_fn):
    """
    Выбираем k-тый элемент в списке l (с нулевой базой)
    :param l: список числовых данных
    :param k: индекс
    :param pivot_fn: функция выбора pivot, по умолчанию выбирает случайно
    :return: k-тый элемент l
    """
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quick_select(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # Нам повезло и мы угадали медиану
        return pivots[0]
    else:
        return quick_select(highs, k - len(lows) - len(pivots), pivot_fn)

def quick_select_median(l, pivot_fn=choice):
    """
    поиск медианы
    :param l: список числовых данных
    :param pivot_fn: функция выбора pivot, по умолчанию выбирает случайно
    """
    if len(l) % 2 == 1:
        return quick_select(l, len(l) / 2, pivot_fn)
    else:
        return 0.5 * (quick_select(l, len(l) / 2 - 1, pivot_fn) + quick_select(l, len(l) / 2, pivot_fn))

length = int(input('Введите размер тестовой выборки: '))
lstTest = [randint(-100, 100) for _ in range(length)]
print(f'length: {len(lstTest)} list:', lstTest)
print('Median:', quick_select_median(lstTest))
lstTest.sort()
print('sorted list: ', lstTest)

