src = not False and True or False and not True

# TODO расписать упрощение выражения

result = True and True or False and False  # упрощение оператора "not"
result = True or False  #  упрощение оператора "and"
result = True  #  упрощение оператора "or"
print(src == result)
