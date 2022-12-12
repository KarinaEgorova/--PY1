from pprint import pprint  # импортируем модуль pprint
#  создаем словарь, где вписываем ключи и их значения
#  используем in range, чтобы словари были для чисел 0-15
dict_translator = [{"bin": bin(i), "dec": i, "hex": hex(i), "oct": oct(i)} for i in range(16)]

pprint(dict_translator)
