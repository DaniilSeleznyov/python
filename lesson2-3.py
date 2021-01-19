if __name__ == '__main__':
    # 3 задание
    seas_list = ['зима', 'весна', 'лето', 'осень']
    seas_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
    month = int(input("Введите месяц от 1 до 12: "))

    if month == 12 or 1 or 2:
        print(seas_list[0])
        print(seas_dict.get(1))

    elif month == 3 or 4 or 5:
        print(seas_list[1])
        print(seas_dict.get(2))

    elif month == 6 or 7 or 8:
        print(seas_list[2])
        print(seas_dict.get(3))

    elif month == 9 or 10 or 11:
        print(seas_list[3])
        print(seas_dict.get(4))
