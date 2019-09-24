#!/usr/bin/env python

with open('D:/Study/3 семестр/Python/7/CAM_table.txt', 'r') as list:
    for k in list:
        if '.' in k:    # если в строке есть точка, то
            vlan, mac, _, intf = k.split()  # присваиваем переменным элементы строки k.split()
            print('{vlan:6} {mac}  {intf}'.format(vlan=vlan, mac=mac, intf=intf))