salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for current_fin in range(1, months + 1):  # обращаемся к range, т.к. надо выполнить действие 10 раз
    current_fin = spend - salary  # расчет недостающей суммы для покрытия расходов
    spend *= (increase + 1)  # учет повышения цен
    need_money += current_fin  # сумма необходимых денег для жизни
print(round(need_money))
