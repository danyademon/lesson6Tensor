def str_to_bytes(_str):
    """
    Переводит список строк в список байт кодов
    
    Параметры:
    _str - список строк
    Возвращает:
    _str - список байт кодов
    """
    for i in range(len(_str)):
        _str[i] = _str[i].encode('utf-8')
    return _str

def bytes_to_str(_bytes):
    """
    Переводит список байт кодов в список строк
    
    Параметры:
    _str - список байт кодов
    Возвращает:
    _str - список строк
    """
    for i in range(len(_bytes)):
        _bytes[i] = _bytes[i].decode('utf-8')
    return _bytes

str_list  = ['привет', 'мир', '!']
print(f'Изначальный список строк: {str_list}')
bytes_list = str_to_bytes(str_list)
print(f'Список байт кодов: {bytes_list}')
str_list = bytes_to_str(bytes_list)
print(f'Список строк после преобразования из байт кодов: {str_list}')