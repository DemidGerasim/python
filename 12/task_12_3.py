from task_12_1 import check_ip_addresses
from task_12_2 import check_list_ip
from tabulate import tabulate


def ip_table(avail, unavail):
    ip_dict = {'Reachable': avail, 'Unreachable': unavail}

    return tabulate(ip_dict, headers='keys')


if __name__ == '__main__':
    ip_list = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    result = check_ip_addresses(check_list_ip(ip_list))
    print(ip_table(result[0], result[1]))