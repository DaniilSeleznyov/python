if __name__ == '__main__':

    my_file = open('task_1.txt', 'w')
    line = input('Введите текст (если закончили нажмите Enter): ')

    while line:
        my_file.writelines(line)
        line = input('Введите текст (если закончили нажмите Enter): ')
        if not line:
            break
    my_file.close()

    my_file = open('task_1.txt', 'r')
    content = my_file.readlines()
    print(content)
    my_file.close()