#!/usr/bin/env python

if __name__ == '__main__':
    tmp = [
        'Protocol:',
        'Prefix:',
        'AD/Metric:',
        'Next-Hop:',
        'Last update:',
        'Outbound Interface:']

    with open('D:/Study/3 семестр/Python/7/ospf.txt', 'r') as f:
        for line in f:
            ospf_list = [x for x
                         in line.replace(',', '').split(' ')  # заменяем запятые пробелами и разделяем значения пробелами.
                         if len(x) > 1]
            ospf_list.insert(0, 'OSPF')

            for t, o in zip(tmp, ospf_list):
                print('{:25}{}'.format(t, o))

            print('\n\n')