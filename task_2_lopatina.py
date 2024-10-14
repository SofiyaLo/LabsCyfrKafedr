from operator import rshift

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_cap = 0
for i in range(10):
    money_cap += spend - salary
    spend *= (1 + increase)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_cap))
