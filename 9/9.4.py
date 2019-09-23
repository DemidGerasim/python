#!/usr/bin/env python3

ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command, ignore):
    return any(word in command for word in ignore)
def get_config(config):
    config_dict = {}
    with open(config, 'r') as file:
        for line in file:
            if ignore_command(line, ignore) or line.find('!') != -1:
                continue
            else:
                if line.startswith(' '):
                    slave = line.strip()
                    config_dict[main].append(slave)
                else:
                    main = line.strip()
                    config_dict[main] = []
    return config_dict
all = get_config('D:/Study/3 семестр/Python/9/config_sw1.txt')
print(all)