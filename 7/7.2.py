#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open('D:/Study/3 семестр/Python/7/config_sw1.txt', 'r') as f:
        lines = [line for line in f.read().split('\n') if '!' not in line]

    for line in lines:
        print(line)
