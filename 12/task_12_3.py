#!/usr/bin/env python3

from tabulate import tabulate

#create two lists
yes = ['192.168.1.{}'.format(i) for i in range(1,10)]
no = ['192.168.9.{}'.format(i) for i in range(1,5)]
def ip_table(list1, list2):
    """
    Функция требует два списка, и распечатать их в табличном
    """
    q = {'Available': [], 'Unavailable': []}
    for i in yes:
        q['Available'].append(i)
    for i in no:
        q['Unavailable'].append(i)
    print(tabulate(q, headers='keys'))

ip_table(yes, no)