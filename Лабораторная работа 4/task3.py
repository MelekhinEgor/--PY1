def delete(list_, index=None):
    if index is None:  # проверяем задан ли индекс, если нет ставим значение по умолчанию -1
        index = -1
        modified_list = list_[:index]
    else:  # если индекс задан то слайсируем список на два - до и после индекса
        modified_list = list_[:index] + list_[(index + 1):]  # объединяем списки в один итоговый
    return modified_list


print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
