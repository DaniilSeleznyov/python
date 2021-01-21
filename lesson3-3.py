if __name__ == '__main__':
    #3 задание
    def my_func(var1 , var2, var3):

        var1 = int(input("Укажите первое значение: "))
        var2 = int(input("Укажите второе значение: "))
        var3 = int(input("Укажите третье значение: "))

        if var1 >= var3 and var2 >= var3:
            return var1 + var2
        elif var1 > var2 or var1 < var3:
            return var1 + var3
        else:
            return var2 + var3


    res = my_func('', '', '')
    print ('Сумма наибольших аргументов: ', res)
