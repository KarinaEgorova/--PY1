def get_count_char(str_):
    symbols_dict = {}   # создаём словарь
    str_ = str_.lower()  # переводим строку в нижний регистр

    for letter in str_:  # перебираем буквы в строке
        if letter.isalpha():  # если символ является буквой
            if letter in symbols_dict:
                symbols_dict[letter] += 1  # символ уже встречался, поэтому количество увеличиваем
            else:
                symbols_dict[letter] = 1  # символ встретился 1 раз
    return symbols_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

symbols_dict = get_count_char(main_str)


def percent_of_symbol(dict_):
    shares_dict = {}  # новый словарь с долями встречаемости каждого символа по отношению ко всем символам
    total_count = sum(dict_.values())  # поиск суммы значений для определения процентного соотношения
    for count in dict_:  # перебираем ключи словаря, далее помещаем ключи в [], чтобы обратиться к значениям
        shares_dict[count] = round(dict_[count] / total_count * 100, 1)  # подсчет процентного соотношения
    return shares_dict


result = percent_of_symbol(symbols_dict)  # помещаем результат выполнения функции в переменную result
print(result)
