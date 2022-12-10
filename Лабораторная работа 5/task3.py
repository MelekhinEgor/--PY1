import random  # подключаем модуль генерации рандомных значений


def get_unique_list_numbers() -> list[int]:
    random_list = []
    count = 0

    while count != 15:  # создаем цикл с проверкой условия - количество символов
        number = random.randint(-10, 10)  # генерируме рандомное цело число в заданном диапазоне
        if number not in random_list:  # задаем условие проверки на уникальность числа
            random_list.append(number)  # добавляем уникальное число в список
            count += 1  # уеличиваем счетчик уникальных символов на единицу
    return random_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
# пустая строка
