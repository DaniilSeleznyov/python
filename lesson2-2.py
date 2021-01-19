if __name__ == '__main__':
    # 2 задание
    swap_list = int(input('Введите количество элементов списка: '))
    my_list = []
    a = 0
    b = 0
    while a < swap_list:
        my_list.append(input("Введите следующее значение списка "))
        a += 1

    for a in range(int(len(my_list)/2)):
        my_list[b], my_list[b + 1] = my_list[b + 1], my_list[b]
        b += 2
    print(my_list)
