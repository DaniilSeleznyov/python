if __name__ == '__main__':
    #1 задание
    def my_split (*args):

        try:
            arg1 = int(input("Укажите числитель: "))
            arg2 = int(input("Укажите знаменатель: "))
            result = arg1 / arg2
        except ValueError:
            return 'Вводите только целочисленные значения!'
        except ZeroDivisionError:
            return 'Выберите другое значение знаменателя! В обычной арифметике на ноль делить нельзя!'

        return result


    print('Результат деления: ', my_split())
