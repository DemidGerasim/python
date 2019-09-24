#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

with open('D:/Study/3 семестр/Python/7/config_sw1.txt', 'r') as f,  open('D:/Study/3 семестр/Python/7/config_sw1_cleared.txt', 'w') as result:
    for list in f:
        for k in ignore:
            if k in list:
                break
        else:
            result.write(list)