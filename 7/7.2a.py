#!/usr/bin/env python

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

with open('D:/Study/3 семестр/Python/7/config_sw1.txt','r') as f:    # Передали название файла скрипту
    for list in f:  # Перебираем каждую строку файла
        if list.startswith('!'):      # перепрыгнули через ! и пошли на начало цикла for
            continue
        for k in ignore:    # перебираем элементы ignore
            if k in list:   # если есть в строке элемент из ignore, то прерываем цикл и переходит к след. строке.
                break
        else:
            print(list)
