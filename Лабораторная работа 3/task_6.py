list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_index = 0  # не поняла, для чего именно мы задаем начальное значение таким образом
for i in range(len(list_numbers)):  #  перебираем все индексы
    max_element = list_numbers[max_index] #  присваиваем переменной максимальный индекс из списка?
    current_element = list_numbers[i]  #  каждый перебираемый иднекс = текущий индекс
    if current_element > max_element:  #  текущий элемент больше максимального?
        max_index = i   # в случае истины, перезаписываем максимальный индекс
list_numbers[max_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_index]  # поменяли местами элементы
print(list_numbers) # выводим список
