#!/usr/bin/env python

vlan_num = input('Введиде номер VLAN: ')
with open('D:/Study/3 семестр/Python/7/CAM_table.txt', 'r') as list:
    for k in list:  # перебираем каждую строку в файле
        if '.' in k: # если есть точка, то
            result = k.split()   # закинули в result содержимое строки
            if result[0] == vlan_num:   # если нулевой элемент равен введённому влану, что выводим 1 и 2 элемены
                print(result[1], result[3])