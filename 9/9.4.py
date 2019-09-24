#!/usr/bin/env python3

ignore = ['duplex', 'alias', 'Current configuration']


def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)

def config(open_cfg):
    with open(open_cfg) as src:
        result = {}
        for line in src:
            if ignore_command(command=line, ignore=ignore) or line.startswith('!'): # если это есть, то продолжаем
                continue
            if not line.startswith(' '):    # если не содержит проблем в начале строки, то
                key = line.strip()  # ключ - строка, в которой убраны whitespace-символы
                result[key] = []    # закидываем в словарь ключ с пустным значением
            else:
                result[key].append(line.strip())    # иначе строка является значением.

    return result

print(config('D:/Study/3 семестр/Python/9/config_sw1.txt'))
