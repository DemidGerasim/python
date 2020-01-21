#!/usr/bin/env python3

import os
from draw_network_graph import draw_topology
from task_11_1 import parse_cdp_neighbors

files = ['D:/Study/Python/11/sh_cdp_n_sw1.txt', 'D:/Study/Python/11/sh_cdp_n_r1.txt',
'D:/Study/Python/11/sh_cdp_n_r2.txt', 'D:/Study/Python/11/sh_cdp_n_r3.txt']
result = {}
for file in files:
    with open(file) as f:
        result.update(parse_cdp_neighbors(f.read()))

# Далее выполняется проверка на дублирование линков.
# Пробегаемся по списку значений словаря
# если элемент списка 'k' соответствует ключу словаря 'result' и значение ключа 'k' словаря 'result'
# содержится в ключе
# то удаляем ключ словаря
for k in list(result.values()):
    if k in result.keys() and result[k] in result.keys():
        del(result[k])
draw_topology(result)
os.startfile(r'D:/Study/Python/11/img/topology.svg')