salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0
current_spend = spend


for month in range(months):

    if salary >= current_spend:

        need_from_capital = 0
    else:

        need_from_capital = current_spend - salary


    money_capital = money_capital + need_from_capital


    current_spend = current_spend * (1 + increase)


money_capital = round(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
