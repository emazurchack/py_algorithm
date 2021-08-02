# -*- coding: utf-8 -*-

print('Задание № 01')

nCompany = int(input('Введите колличество компаний: ').strip())
dCompanyData = {i: {'name': input('Наименование компании: ').strip(),
                    'profit': [*map(float, input(f'Введите значения прибыли за 4 квартала ("точка" - для дробной части)').split())],
                    'sum': 0,
                    'avg': 0
               } for i in range(nCompany)}
for cd in dCompanyData.keys():
    dCompanyData[cd]['sum'] = sum(dCompanyData[cd]['profit'])
    dCompanyData[cd]['avg'] = dCompanyData[cd]['sum'] / len(dCompanyData[cd]['profit'])

nAVGForAll = sum([dCompanyData[i]['avg'] for i in dCompanyData.keys()]) / len(dCompanyData.keys())

print(dCompanyData)
print(f'AVG for All companies: {nAVGForAll}')
# -- greatest then nAVGForAll
print(f'Companies AVG profit greatest then {nAVGForAll}: ', [dCompanyData[i]['name'] for i in dCompanyData.keys() if dCompanyData[i]['avg'] > nAVGForAll])
# -- least then nAVGForAll
print(f'Companies AVG profit least then {nAVGForAll}: ', [dCompanyData[i]['name'] for i in dCompanyData.keys() if dCompanyData[i]['avg'] < nAVGForAll])


print('Задание № 02')
class Hex(object):
    def __init__(self, item):
        self.item = hex(int(item, 16))
    def __str__(self):
        return f'{str(self.item).upper()}'
    def __add__(self, other):
        return Hex(hex(int(self.item, 16) + int(other.item, 16)))
    def __sub__(self, other):
        return Hex(hex(int(self.item, 16) - int(other.item, 16)))
    def __mul__(self, other):
        return Hex(hex(int(self.item, 16) * int(other.item, 16)))
    def asList(self):
        return([s for s in self.item])

a = Hex('A2')
print(f'"a" as Str: {a}, as List: {a.asList()}')
b = Hex('C4F')
print(f'"b" as Str: {b}, as List: {b.asList()}')
print(f'"a+b"as Str: {a+b}, as List: {(a+b).asList()}')
print(f'"a-b"as Str: {a-b}, as List: {(a-b).asList()}')
print(f'"a*b"as Str: {a*b}, as List: {(a*b).asList()}')
