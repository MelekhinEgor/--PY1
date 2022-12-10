from pprint import pprint  # подключаем функцию pprint из модуля pprint

numbers_dicts_set = []  # вводим пустой список

for number in range(16):
    numbers_dicts_set.append({
        "bin": bin(number),  # переводим в двоичное число
        "dec": number,  # десятичное число
        "hex": hex(number),  # переводим в шестнадцатеричное число
        "oct": oct(number)  # переводим в восьмеричное число
    })

pprint(numbers_dicts_set)
# пустая строка
