"""
Использовать encrypt и decrypt
для шифрования и дешифровки соответственно
"""


def text_to_bit_array(text):
    """
    Создаёт из строки список бит
    :param text: строка текста (str)
    :return: список бит (list)
    """
    return list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in text])))


def bit_array_to_text(bit_array):
    """
    Создаёт из списка бит строку
    :param bit_array: список бит (list)
    :return: строка (str)
    """
    return ''.join(chr(int(''.join(map(str, bit_array[i:i + 8])), 2)) for i in range(0, len(bit_array), 8))


def function(text, password):
    """
    Преобразует текст по данному паролю
    :param text: текст (str)
    :param password: пароль (str)
    :return: преобразованный текст (str)
    """
    password_bit_array = text_to_bit_array(password)
    text_bit_array = text_to_bit_array(text)
    result = list()
    for i in range(len(text_bit_array)):
        result.append(text_bit_array[i] ^ password_bit_array[i % len(password)])
    return bit_array_to_text(result)


def encrypt(text, password):
    """
    Шифрует текст по заданному паролю
    :param text: строка исходного текста (str)
    :param password: пароль (str)
    :return: строка зашифрованного текста (str)
    """
    return function(text, password)


def decrypt(text, password):
    """
    Дешифрует текст по заданному паролю
    :param text: строка (str)
    :param password: пароль (str)
    :return: строка исходного текста (str)
    """
    return function(text, password)
