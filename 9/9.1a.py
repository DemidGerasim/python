#!/usr/bin/env python3


def generate_access_config(access, psecurity=None):
    lists = []  # создали пустой список
    '''
       access - словарь access-портов,
       для которых необходимо сгенерировать конфигурацию, вида:
           { 'FastEthernet0/12':10,
             'FastEthernet0/14':11,
             'FastEthernet0/16':17 }
       psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
           - если значение True, то настройка выполняется с добавлением шаблона port_security
           - если значение False, то настройка не выполняется
       Возвращает список всех команд, которые были сгенерированы на основе шаблона
       '''
    access_mode_template = ['switchport mode access',
                            'switchport access vlan',
                            'switchport nonegotiate',
                            'spanning-tree portfast',
                            'spanning-tree bpduguard enable']
    port_security_template = ['switchport port-security maximum 2',
                              'switchport port-security violation restrict',
                              'switchport port-security']
    for inter, vlan in access.items():
        lists.append('interface {}'.format(inter))
        for template in access_mode_template:
            if template.endswith('access vlan'):
                lists.append(template + ' {}'.format(vlan))
            else:
                lists.append(template)
        for sec in port_security_template:
            if psecurity:
                lists.append(sec)
    return lists


access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17}
print(generate_access_config(access_config, psecurity=True))
