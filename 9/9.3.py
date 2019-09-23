#!/usr/bin/env python3

def get_int_vlan_map(config):
    with open(config, 'r') as file:
            access_config = {}
            for line in file:
                if line.find('FastEthernet') != -1:
                    interface = line.split()[-1]
                elif line.find('access vlan') != -1:
                    access_vlan = line.split()[-1]
                    access_config[interface] = access_vlan
                else:
                    pass
            print('access interfaces: \n', access_config)
            return access_config
get_int_vlan_map('D:/Study/3 семестр/Python/9/config_sw1.txt')