if __name__ == '__main__':
    #5 задание
    def my_sum():
        sum_res = 0
        em = False
        while em == False:
            number = input('Введите числа для сложения через пробел, для выхода введите Q: ').split()

            res = 0
            for el in range(len(number)):
                if number[el] == 'q' or 'Q':
                    em = True
                    break
                else:
                    res = res + int(number[el])
            sum_res = sum_res + res
            print(f'Текущая сумма: {sum_res}')
        print(f'Окончательная сумма: {sum_res}')


    my_sum()
