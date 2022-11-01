def delete(list_, index=None):
    if index is not None:  #  если пользователь указал индекс
        list_ = list_[:index] + list_[index + 1:]  # складываем две части списка за исключением удаляемого значения
    else:
        list_ = list_[:-1]  # если пользователь не указал индекс, по умолчанию удаляем последний элемент
    return list_

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
