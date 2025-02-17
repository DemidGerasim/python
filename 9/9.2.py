#!/usr/bin/env python3

def generate_trunk_config(trunk):
    lists = [] # создали пустой список
    '''
    trunk - словарь trunk-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/1':[10,20],
          'FastEthernet0/2':[11,30],
          'FastEthernet0/4':[17] }
    Возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    '''
    trunk_mode_template = ['switchport trunk native vlan 999',
                  'switchport trunk allowed vlan'] 
    for inter, vlan in trunk.items():  
        lists.append('interface {}'.format(inter))
        for template in trunk_mode_template:
          if template.endswith('allowed vlan'):
              vlan = [str(num) for num in vlan]
              vlan = ','.join(vlan)
              lists.append(template + ' {}'.format(vlan))
          else:
              lists.append(template)
    print(lists)
    return lists

trunk_config = {'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }

generate_trunk_config(trunk_config)