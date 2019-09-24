#!/usr/bin/env python
from sys import argv

with open('D:/Study/3 семестр/Python/7/config_sw1.txt','r') as f:    # Передали название файла скрипту
    for list in f:
        if list.startswith('!'):        # перепрыгнули через ! и пошли в начало цикла for
            continue
        print(list, end="")