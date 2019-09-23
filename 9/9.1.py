#!/usr/bin/env python3

def generate_access_config(access):
    lists = []
    access_template = ['switchport mode access',
                   'switchport access vlan',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']
    for inter, vlan in access.items():
        lists.append('interface {}'.format(inter))
        for template in access_template:
            if template.endswith('access vlan'):
                lists.append(template + ' {}'.format(vlan))
            else:
                lists.append(template)
    return lists

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17}
lists = generate_access_config(access_config)
print(lists)