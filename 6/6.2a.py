#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    ip_addr = input('Enter ip address: ')
    if ip_addr is False:
        print('Enter non empty address')
        exit()

    ip_list = ip_addr.split('.')
    if (len(ip_list) != 4):
        print('Enter correct ip string')
        exit()

    try:
        prefix = int(ip_list[0])
    except ValueError:
        print('{} is not a valid number'.format(ip_list[0]))
        exit()

    if (prefix >= 1 and prefix <= 223):
        print('unicast')
    elif (prefix >= 224 and prefix <= 239):
        print('multicast')
    elif (ip_addr == '255.255.255.255'):
        print('local broadcast')
    elif(ip_addr == '0.0.0.0'):
        print('unassigned')
    else:
        print('unused')
