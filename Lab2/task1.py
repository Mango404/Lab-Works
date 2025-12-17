money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0
current_capital = money_capital
current_spend = spend


while True:

    budget = salary + current_capital

    if budget < current_spend:
        break

    current_capital = budget - current_spend

    months +=  1

    current_spend = current_spend * (1 + increase)

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", months)