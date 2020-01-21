def get_int_vlan_map(config_file):
    with open(config_file) as src:
        config = {}
        for line in src:  # Пробегаемся по каждой строке в файле
            if line.startswith('interface'):  # Ищем строку, где встречается нужно слово
                interface = line.split(' ')[1].strip()
                config[interface] = []  # создаём пустой словарь, где ключ interface
            elif line.startswith(' '):
                config[interface].append(line.strip())  # Добавляем в словарь значения (конфиг интерфейса)

    access_ports = {}

    for interface, comand in config.items():  # закидываем в переменные ключ и значения словаря
        for k in comand:
            if k.startswith('switchport access'):
                access_ports[interface] = int(k.split()[-1])  # Если встречается строка, то кидаем в значение номер влан
            elif 'switchport mode access' in k:     # если не первые два условия, то сработает это условие
                access_ports[interface] = int(1)    # закидываем в значение ключа единичку

    return access_ports

print(get_int_vlan_map('D:/Study/Python/9/config_sw2.txt'))  