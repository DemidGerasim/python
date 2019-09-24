#!/usr/bin/env python3

from draw_network_graph import draw_topology
from task_11_1 import parse_cdp_neighbors

with open('D:/Study/3 семестр/Python/11/sw1_sh_cdp_neighbors.txt') as src:
    src_file = src.read()

draw_topology(parse_cdp_neighbors(src_file))    # Передали как аргумен вывод функции parse_cdp_neibors

files = ['D:/Study/3 семестр/Python/11/sh_cdp_n_sw1.txt', 'D:/Study/3 семестр/Python/11/sh_cdp_n_r1.txt',
'D:/Study/3 семестр/Python/11/sh_cdp_n_r2.txt', 'D:/Study/3 семестр/Python/11/sh_cdp_n_r3.txt']
result = {}
for file in files:
    with open(file) as f:
        result.update(parse_cdp_neighbors(f.read()))

# Далее выполняется проверка на дублирование линков.
# Пробегаемся по списку значений словаря
# если элемент списка 'k' соответствует ключу словаря 'result' и значение ключа 'k' словаря 'result' содержится в ключе
# то удаляем ключ словаря
for k in list(result.values()):
    if k in result.keys() and result[k] in result.keys():
        del(result[k])

draw_topology(result)