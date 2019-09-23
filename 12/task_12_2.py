from task_12_1 import check_ip_addresses


def check_list_ip(ip_list):
    """ Функция проверяет, присутствует ли диапазон айпишников
    в каком-либо элементе списка и, если он есть, то "разворачивает его".
    While используется, чтобы делать проверку для каждого элемента списка,
    так как диапазонов может быть несколько. Возвращает обновлённый список.
    """
    i = len(ip_list)
    while i > 0:
        for ip in ip_list:
            if '-' in ip:
                ip_begin = ip.split('-')[0].rsplit('.', maxsplit=1)[0]  # первые три неизменяемых октета в диапазоне
                if len(ip.split('-')[1]) > 3:   # проверка, как задан диапазон. Такой ли вид 127.0.0.1-127.0.0.3 ?
                    ip_list.remove(ip)  # удаляем из списка этот диапазон, чтобы немножились записи результата
                    ip = ip.split('-')
                    rng = []
                    for j in ip:
                        rng.append(j.rsplit('.', maxsplit=1)[-1])   # ищем границы диапазона
                else:
                    ip_list.remove(ip)  # удаляем из списка этот диапазон, чтобы немножились записи результата
                    rng = ip.rsplit('.', maxsplit=1)[1].split('-')  # ищем границы диапазона
                octet_range = [i for i in range(int(rng[0]), int(rng[1]) + 1)]  # "Разворачиваем диапазон rng[n,m]
                for k in octet_range:
                    ip_list.append(ip_begin + '.' + str(k))     # скидываем в список итоговые айпишники
        i -= 1
    return ip_list


if __name__ == '__main__':
    ip_list = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    result = check_ip_addresses(check_list_ip(ip_list))
    print(f'Available IP: {result[0]} \nUnavailable IP: {result[1]}')