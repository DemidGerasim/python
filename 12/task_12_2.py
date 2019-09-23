#!/usr/bin/env python3

import subprocess
import argparse
import multiprocessing
from multiprocessing import Process
from task_12_1 import check_ip_addresse
from task_12_1 import ping_ip_list


def count_integer(a, b):
    """
    Эта функция считает количество объектов между переменными a и b.
    """
    x = 0
    status = True
    while status:
        if a == b:
            x = x + 1
            status = False
        else:
            a = a + 1
            x = x + 1
    return x

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Ping script')
    parser.add_argument('ip', action='store', help='Enter ip-address-list just like: 8.8.4.4 or 172.21.41.128-172.21.41.132 or 1.1.1.1-3')
    args = parser.parse_args()

    ip_list = []
    if '-' in args.ip:
        ip_str, ip_str2 = args.ip.split('-')
        last_oktet = int(ip_str.split('.')[-1])
        last_oktet2 = int(ip_str2.split('.')[-1])
        x = count_integer(last_oktet, last_oktet2)
        ip_str = ip_str.split('.')
        ip_int = [int(i) for i in ip_str]

        for i in range(x):
            ip_str = [str(i) for i in ip_int]
            ip_str = '.'.join(ip_str)
            ip_list.append(ip_str)
            ip_int[-1] = ip_int[-1] + 1

        print(ping_ip_list(ip_list))
    else:
        result = {True: [], False: []}
        command = subprocess.run('ping -c 3 {}'.format(args.ip), shell=True, stdout=subprocess.DEVNULL)
        if command.returncode == 0:
            print('Yeah,', args.ip, 'is alive')
            result[True].append()
        else:
            print('Oh noo,'. args.ip, 'is dead')