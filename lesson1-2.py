if __name__ == '__main__':
    # 2 задание
    print("Введите время в секундах: ")
    n = int(input())
    def convert(seconds):
        min, sec = divmod(seconds, 60)
        hour, min = divmod(min, 60)
        return "%d:%02d:%02d" % (hour, min, sec)
    print(convert(n))
