import string  # подключаем модуль strin чтобы получить алфавиты букв и цифр
from random import sample  # подключаем функцию sample из модуля randome


def get_random_password(n=None) -> str:
    chars = string.digits + string.ascii_letters  # собираем алфавит, откуда будут браться символы

    if n is None:  # задаем длину пароля по умолчанию, если она не задана
        n = 8

    random_password = ''.join(sample(chars, n))  # генерируем пароль, используем .join чтобы была одна строка
    return random_password


print(get_random_password())
# пустая строка
