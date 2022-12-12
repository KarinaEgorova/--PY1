def get_unique_list_numbers() -> list[int]:
    from random import shuffle
    # использование функции shuffle для генерации случайного списка (перемешанной последовательности)
    list_ = [i for i in range(-10, 10)]  # выставляем необходимый диапазон случайных чисел
    shuffle(list_)
    return list_[:15]  # устанавливаем размер списка


list_unique_numbers = get_unique_list_numbers()

print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
