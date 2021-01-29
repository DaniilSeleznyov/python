if __name__ == '__main__':

    dict = {}

    with open('task_6.txt', 'r', encoding='utf-8') as init_f:
        for line in init_f:
            subject, lecture, practice, lab = line.split()
            dict[subject] = int(lecture) + int(practice) + int(lab)

        print(f'Количество часов по предметам -\n{dict}')
