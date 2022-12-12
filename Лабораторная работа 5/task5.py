def get_random_password() -> str:
    import random
    import string
    n = 8  # заданная длина пароля
    # подтягиваем элементы для пароля
    password_symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits
    # генерируем пароль
    password = "".join(random.sample(password_symbols, n))
    return password


print(get_random_password())
