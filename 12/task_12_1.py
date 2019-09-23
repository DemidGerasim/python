#!/usr/bin/env python3

import subprocess
import multiprocessing
from multiprocessing import Process

def check_ip_addresse(ip, queues):
    """
    Функция требует IP и класса Queue. Пингуйте IP и ставьте результат в очереди объекта.
    """
    command = subprocess.run('ping -c 3 {}'.format(ip), shell=True, stdout=subprocess.DEVNULL)
    if command.returncode == 0:
        print('Yeah,', ip, 'is alive.')
        status = True
    else:
        print('Oh noo,', ip, 'is dead.')
        status = False
    queues.put((status, ip))
def ping_ip_list(ip_list):
    """
    Функция требует список строк, таких как IP.
    """
    queues = multiprocessing.Queue()
    procs = []
    result = {True:[], False:[]}

    for ip in ip_list:
        p = Process(target=check_ip_addresse, args=(ip, queues))
        procs.append(p)
        p.start()

    for p in procs:
        p.join()

    for p in procs:
        key, value = queues.get()
        result[key].append(value)
    return result
if __name__ == '__main__':
    ip_lists = ['192.168.0.1', '74.125.143.113', '74.125.143.113-74.125.143.115', '74.125.143.111-113']
    print(ping_ip_list(ip_lists))