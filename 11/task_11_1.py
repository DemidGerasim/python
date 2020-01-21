#!/usr/bin/env python3

def parse_cdp_neighbors(src_file):
    list = src_file.split('\n')
    local_device = list[0].split('>')[0]  # нулевую строку разделяем и берём первый элемент
    result = {}
    for line in list:
        if '/' in line:
            remote_device = line.split()[0]
            local_interface = line.split()[1] + line.split()[2]  # собираем интерфейс вида fa0/0
            remote_interface = line.split()[-2] + line.split()[-1]  # собираем интерфейс вида fa0/0.
            result[local_device, local_interface] = (remote_device, remote_interface)
    return result


# Если функция запускается как самостоятельный элемент, а не импортируется куда-то как модуль,
#  то выполняется следующее
if __name__ == '__main__':
    with open('D:/Study/Python/11/sw1_sh_cdp_neighbors.txt') as src:  # открывает указанный файл
        src_file = src.read()  # считываем открытый файл и кидаем его в переменную
    print(parse_cdp_neighbors(src_file))  # выводим результат работы функции, с аргументом file