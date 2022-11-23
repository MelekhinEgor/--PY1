salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

for i in range(months):
    delta = spend - salary  # находим разницу между расходами и доходами
    money_capital += delta  # добавляем разницу в подушку безопасности
    spend *= 1 + increase  # увеличиваем расходы в месяц

print(round(money_capital))
