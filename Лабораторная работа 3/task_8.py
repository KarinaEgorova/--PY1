money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
delta = salary - spend  # в текущий месяц потрачено больше, чем покрывает ЗП
money_capital += delta  # -1000 из финансовой подушки для покрытия расходов

while money_capital >= 0:  # выполняем, пока финансовая подушка положительна
    spend *= (increase + 1)  # увеличение расходов в связи с ростом цен
    delta = salary - spend
    money_capital += delta
    month += 1  # пока выполняется условие, увеличивается кол-во месяцев

print(month)
