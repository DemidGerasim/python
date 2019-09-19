#!/usr/bin/env python3

def parse_cdp_neighbors(show):
    with open(show) as file:
        show = file.read()
        q = {}
        show = show.split('\n')
        for line in show:
            main = []
            second = []
            if line.find('>') != -1:
                main_machine = line[:line.find('>')]
            elif line.find('Eth') != -1:
                second_machine, main_eth, main_inter, *other, second_eth, second_inter = line.split()
                main.append(main_machine)
                second.append(second_machine)
                main_interface = main_eth + main_inter
                second_interface = second_eth + second_inter
                main.append(main_interface)
                second.append(second_interface)
                main_tuple = tuple(main)
                second_tuple = tuple(second)
                q[main_tuple] = second_tuple
    return q
if __name__ == "__main__":
    q = parse_cdp_neighbors('D:/Study/3 семестр/Python/11/sw1_sh_cdp_neighbors.txt')
    print(q)