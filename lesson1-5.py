if __name__ == '__main__':
    # 5 задание
    profit = int(input("Введите значение выручки фирмы: "))
    costs = int(input("Введите значение издержек фирмы: "))
    if profit > costs:
        print('Фирма в плюсе')
        rent = ((profit-costs) // profit)
        print('Рентабельность выручки', rent)
    elif profit < costs:
        print('Фирма убыточна')
    group = int(input("Численность сотрудников фирмы: "))
    profone = ((profit-costs) // group)
    print('Прибыль фирмы в перерасчете на одного сотрудника: ', profone)
