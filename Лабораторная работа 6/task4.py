import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(csv_file, delimiter=',', new_line='\n') -> list[dict]:
    list_dicts = []  # создаем новый список словарей

    with open(csv_file) as f:  # открываем файл
        header = f.readline()  # считываем первую строку из файла с данными "шапки"
    # создаем лист заголовков, разделяя запятыми,
    # чтобы далее использовать его как "название" к значениям
    # разделитель строк по умолчанию заменяем на пробел
        headers_list = header.replace(new_line, "").split(delimiter)
        for row in f:  # проходимся по строкам
    # добавляем в лист словари с помощью dict
    # и zip для объединения элементов (ключей-заголовков и значений-строк)
            list_dicts.append(dict(zip(headers_list, row.replace(new_line, "").split(delimiter))))

    return list_dicts


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
