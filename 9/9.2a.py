#!/usr/bin/env python3

def generate_trunk_config(trunk):
    trunk_mode_template = ['switchport trunk native vlan 999',
              'switchport trunk allowed vlan'] 
    dicall = {}
    for inter, vlan in trunk.items():
        dicall[inter] = []
        for template in trunk_mode_template:
            if template.endswith('allowed vlan'):
                vlan = [str(num) for num in vlan]
                vlan = ','.join(vlan)
                dicall[inter].append(template + " {}".format(vlan))
            else:
                dicall[inter].append(template)
    print(dicall)
    return(dicall)
trunk_config = {'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }

generate_trunk_config(trunk_config)