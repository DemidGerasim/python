#!/usr/bin/env python3

def get_int_vlan_map(config):
    access_config = {}
    with open(config, 'r') as file:
        for line in file:
            if line.find('FastEthernet') != -1:
                interface = line.split()[-1]
                line = file.readline()
                if line.find('mode access') != -1:
                    line = file.readline()
                    access_vlan = line.split()[-1]
                    if access_vlan.isdigit():
                        access_config[interface] = access_vlan
                    else:
                        access_config[interface] = '1'
                elif line.find('encapsulation dot1q') != -1:
                    line = file.readline()
                    print('access interfaces: \n', access_config)
        return access_config
get_int_vlan_map('D:/Study/3 семестр/Python/9/config_sw2.txt')