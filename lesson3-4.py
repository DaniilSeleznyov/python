if __name__ == '__main__':
    #4 задание
    def my_func(x, y):
        x = float(input("Укажите действительное положительное число: "))
        y = int(input("Укажите целое отрицательное число (степень): "))
        res = (x**y)

        return res
# 2 вариант
    # def x_pow(x, y)

# 3 вариант. С помощью использования циклов:
#     x = float(input("Укажите действительное положительное число: "))
#     y = int(input("Укажите целое отрицательное число (степень): "))
#     res = 1
#     while (y < 0):
#         res *= 1/x
#         y -= -1

    res = my_func("", "")
    print ('Результат возведения: ', res)
