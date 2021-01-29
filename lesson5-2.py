if __name__ == '__main__':

    my_file = open('task_2.txt', 'r')
    content = my_file.read()
    print(f'Содержимое файла: \n\n{content}\n')

    my_file = open('task_2.txt', 'r')
    content = my_file.readlines()
    print(f'Количество строк в файле - {len(content)}\n')

    my_file = open('task_2.txt', 'r')
    content = my_file.readlines()
    for line in content:
        Type = line.split("\n")
        x = Type[0]
        i = x.split()
        print('Количество слов --', len(i))

    my_file.close()
