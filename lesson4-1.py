from sys import argv

name, prod, bet, bonus = argv
try:
    prod = int(prod)
    bet = int(bet)
    bonus = float(bonus)
    res = prod * bet + bonus
    print ('Выработка в часах: ', prod)
    print('Ставка (за час): ', bet)
    print('Премиальные: ', bonus)
    print(f'Заработная плата сотрудника:  {round(res, 2)}')
except ValueError:
    print('Введенные параметры ошибочны!')
