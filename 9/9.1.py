#!/usr/bin/env python3

def generate_access_templates(access):
    lists = [] # создали пустой список
    access_template = ['switchport mode access',
                   'switchport access vlan',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']
    for inter, vlan in access.items(): # перебираем словрь и закидываем в переменные ключ: значение
        lists.append('interface {}'.format(inter))
        for template in access_template: # Пробегаемся по шаблону
            if template.endswith('access vlan'):  # Если заканчивается на vlan
                lists.append(template + ' {}'.format(vlan)) # то в строке добавляем значение словаря access_config,
                #то есть номер влана
            else:
                lists.append(template)
    return lists

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17}
lists = generate_access_templates(access_config)
print(lists)