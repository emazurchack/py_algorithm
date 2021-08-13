# -*- coding: utf-8 -*-

import sys
import platform
_ids_ = set()

def getDeepSizeOf(o, ids):
    if id(o) in ids:
        return 0

    r = sys.getsizeof(o)
    ids.add(id(o))

    if isinstance(o, str):  #or isinstance(0, unicode):
        #print('size of string:', o)
        return r
    if isinstance(o, int):
        #print('size of int:', o)
        return r
    if isinstance(o, float):
        #print('size of float:', o)
        return r
    if isinstance(o, list):
        #print('size of list:', o)
        return r + sum(getDeepSizeOf(x, ids) for x in o)
    if isinstance(o, tuple):
        #print('size of tuple:', o)
        return r + sum(getDeepSizeOf(x, ids) for x in o)
    if isinstance(o, set) or isinstance(o, frozenset):
        # print('size of tuple:', o)
        return r + sum(getDeepSizeOf(x, ids) for x in o)
    if isinstance(o, dict):
        #print('size of dict:', o)
        return r + sum(getDeepSizeOf(i, ids) + getDeepSizeOf(o[i], ids) for i in o.keys())
    #print(r)
    return r

"""
nCompany = int(input('Введите колличество компаний: ').strip())
dCompanyData = {i: {'name': input('Наименование компании: ').strip(),
                    'profit': [*map(float, input(f'Введите значения прибыли за 4 квартала ("точка" - для дробной части)').split())],
                    'sum': 0,
                    'avg': 0
               } for i in range(nCompany)}
"""
nCompany = 3
dCompanyData = {0: {'name': 'рога', 'profit': [123.45, 6345.44, 768.99, 7648.11], 'sum': 0, 'avg': 0},
         1: {'name': 'копыта', 'profit': [897.77, 347.66, 53623.33, 89576.43], 'sum': 0, 'avg': 0},
         2: {'name': 'зачет', 'profit': [2342.09, 94587.05, 7634.32, 3457.01], 'sum': 0, 'avg': 0}}
##
print('Версии:')
print('ОС:', platform.platform(aliased=True), )
print(f'Python: {str(sys.version_info.major)}.{str(sys.version_info.minor)}.{str(sys.version_info.micro)}')
print('')
for cd in dCompanyData.keys():
    dCompanyData[cd]['sum'] = sum(dCompanyData[cd]['profit'])
    dCompanyData[cd]['avg'] = dCompanyData[cd]['sum'] / len(dCompanyData[cd]['profit'])

nAVGForAll = sum([dCompanyData[i]['avg'] for i in dCompanyData.keys()]) / len(dCompanyData.keys())

print('Данные:', dCompanyData)
print('')
print('Вывод:')
print(f'AVG for All companies: {nAVGForAll}')
# -- greatest then nAVGForAll
print(f'Companies AVG profit greatest then {nAVGForAll}: ', [dCompanyData[i]['name'] for i in dCompanyData.keys() if dCompanyData[i]['avg'] > nAVGForAll])
# -- least then nAVGForAll
print(f'Companies AVG profit least then {nAVGForAll}: ', [dCompanyData[i]['name'] for i in dCompanyData.keys() if dCompanyData[i]['avg'] < nAVGForAll])
##
print('')
print('Анализ используемой памяти:')
fDataSize = getDeepSizeOf(nCompany, _ids_) + getDeepSizeOf(dCompanyData, _ids_) + getDeepSizeOf(nAVGForAll, _ids_)
print('Занимаемая память под структуры и переменные программы: ', fDataSize)
fPrintDataSize = getDeepSizeOf([dCompanyData[i]['name'] for i in dCompanyData.keys() if dCompanyData[i]['avg'] > nAVGForAll], _ids_) + \
                 getDeepSizeOf([dCompanyData[i]['name'] for i in dCompanyData.keys() if dCompanyData[i]['avg'] < nAVGForAll], _ids_)
fAVGCalcSize = getDeepSizeOf([dCompanyData[i]['avg'] for i in dCompanyData.keys()], set()) + getDeepSizeOf(dCompanyData.keys(), _ids_)
print('Для расчета среднего:', fAVGCalcSize)
print('Для вывода компаний по условиям:', fPrintDataSize)
print('Всего:', fDataSize + fPrintDataSize + fAVGCalcSize, 'байт')
"""
Версии:
ОС: Windows-10-10.0.19042-SP0
Python: 3.9.5

Данные: {0: {'name': 'рога', 'profit': [123.45, 6345.44, 768.99, 7648.11], 'sum': 14885.989999999998, 'avg': 3721.4974999999995}, 1: {'name': 'копыта', 'profit': [897.77, 347.66, 53623.33, 89576.43], 'sum': 144445.19, 'avg': 36111.2975}, 2: {'name': 'зачет', 'profit': [2342.09, 94587.05, 7634.32, 3457.01], 'sum': 108020.46999999999, 'avg': 27005.117499999997}}

Вывод:
AVG for All companies: 22279.304166666665
Companies AVG profit greatest then 22279.304166666665:  ['копыта', 'зачет']
Companies AVG profit least then 22279.304166666665:  ['рога']

Анализ используемой памяти:
Занимаемая память под структуры и переменные программы:  2316
Для расчета среднего: 200
Для вывода компаний по условиям: 88
Всего: 2604 байт
"""
