# -*- coding: utf-8 -*-
"""
1. Определение количества различных подстрок с использованием хэш-функции.
    Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
    Требуется найти количество различных подстрок в этой строке.
2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
print('Задание № 01')
from hashlib import sha1

def countSubStr(string):
    str_length = len(string)
    assert str_length, "Строка не может быть пустой"

    is_counted = [
        string
    ]
    substrings = {}

    # формируем подстроки
    for pos in range(str_length):
        for width in range(pos + 1, str_length + 1):
            subs = string[pos:width]
            if subs not in is_counted and subs not in substrings:
                substrings[subs] = 0

    for patt in substrings:
        patt_length = len(patt)
        patt_hash = sha1(patt.encode("utf-8")).hexdigest()
        for i in range(str_length - patt_length + 1):
            subs_hash = sha1(string[i:i + patt_length].encode("utf-8")).hexdigest()
            if subs_hash == patt_hash:
                substrings[patt] += 1

    return substrings


s = input("Введите строку: ")

result = countSubStr(s)
print(result)
print(f"Количество подстрок {sum(x for x in result.values())}")

print('Задание № 02')
import heapq  # модуль для работы с мин. кучей из стандартной библиотеки Python
from collections import Counter  # словарь в котором для каждого объекта поддерживается счетчик
from collections import namedtuple

# классы для хранения информации о структуре дерева
class Node(namedtuple("Node", ["left", "right"])):  # класс для ветвей дерева - внутренних узлов; у них есть потомки
    def walk(self, code, acc):
        # чтобы обойти дерево нам нужно:
        self.left.walk(code, acc + "0")  # пойти в левого потомка, добавив к префиксу "0"
        self.right.walk(code, acc + "1")  # затем пойти в правого потомка, добавив к префиксу "1"

class Leaf(namedtuple("Leaf", ["char"])):  # класс для листьев дерева, у него нет потомков, но есть значение символа
    def walk(self, code, acc):
        # потомков у листа нет, по этому для значения мы запишем построенный код для данного символа
        code[self.char] = acc or "0"  # если строка длиной 1 то acc = "", для этого случая установим значение acc = "0"

def hf_encode(s):  # функция кодирования строки в коды Хаффмана
    h = []
    print('Таблица частот:')
    for ch, freq in Counter(s).items():
        print('ch=', ch, ' freq=', freq)
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:  # пока в очереди есть хотя бы 2 элемента
        freq1, _count1, left = heapq.heappop(h)  # вытащим элемент с минимальной частотой - левый узел
        freq2, _count2, right = heapq.heappop(h)  # вытащим следующий элемент с минимальной частотой - правый узел
        # поместим в очередь новый элемент, у которого частота равна суме частот вытащенных элементов
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right))) # добавим новый внутренний узел у которого потомки left и right соответственно
        count += 1  # инкрементируем значение счетчика при добавлении нового элемента дерева
    code = {}  # инициализируем словарь кодов символов
    if h:  # если строка пустая, то очередь будет пустая и обходить нечего
        [(_freq, _count, root)] = h
        root.walk(code, "")  # обойдем дерева от корня и заполним словарь для получения кодирования Хаффмана
    return code  # возвращаем словарь символов и соответствующих им кодов

def hf_decode(encoded, code):  # функция декодирования исходной строки по кодам Хаффмана
    decode_chars, encode_char = [], ""
    for ch in encoded:
        encode_char += ch
        for dec_ch in code:
            if code.get(dec_ch) == encode_char:
                decode_chars.append(dec_ch)
                encode_char = ""
                break
    return "".join(decode_chars)  # значение раскодированной строки

def Test():
    # кодирования строки в коды Хаффмана
    print('Тест кодирования строки в коды Хаффмана')
    s = 'Рядом с садом китайского императора, в лесу жил соловей, пение которого было настолько прекрасно, что о нем говорили все и даже писали в книгах. Император пожелал, чтобы соловей жил в его дворце, но вскоре заменил его на игрушечного золотого соловья. И хотя с настоящим соловьем обошлись очень плохо, он всё же помог вскоре избежать смерти императора... '
    print('Строка для кодирования:', s)
    code = hf_encode(s)  # кодируем строку
    encoded = "".join(code[ch] for ch in s)  # отобразим закодированную версию, отобразив каждый символ
                                             # в соответствующий код и конкатенируем результат
    print('число символов:', len(code), 'длина закодированной строки:', len(encoded))
    print('')
    print('Таблица кодов:')
    for ch in sorted(code): # обойдем символы в словаре в алфавитном порядке с помощью функции sorted()
        print("{}: {}".format(ch, code[ch]))  # выведем символ и соответствующий ему код

    print('')
    print('Закодированная строка:', encoded)  # выведем закодированную строку

    assert hf_decode(encoded, code) == s  # раскодируем строку и сравним ее с исходной строкой

def main():
    s = input('Введите строку для кодирования: ')  # читаем строку длиной  до 10**4
    print('Строка для кодирования:', s)
    code = hf_encode(s)  # кодируем строку
    encoded = "".join(code[ch] for ch in s)  # отобразим закодированную версию, отобразив каждый символ
                                             # в соответствующий код и конкатенируем результат
    print('число символов:', len(code), 'длина закодированной строки:', len(encoded))
    print('')
    print('Таблица кодов:')
    for ch in sorted(code): # обойдем символы в словаре в алфавитном порядке с помощью функции sorted()
        print("{}: {}".format(ch, code[ch]))  # выведем символ и соответствующий ему код

    print('')
    print('Закодированная строка:', encoded)  # выведем закодированную строку

    assert hf_decode(encoded, code) == s  # раскодируем строку и сравним ее с исходной строкой
"""
if __name__ == "__main__":
    main()
"""
Test()
