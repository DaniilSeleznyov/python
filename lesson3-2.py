if __name__ == '__main__':
    #2 задание
    def my_doc (name, surname, year, city, email, number):
        name = input('Введите Ваше имя: ')
        surname = input('Введите Вашу фамилию: ')
        year = int(input('Введите Ваш год рождения: '))
        city = input('Введите Ваш город проживания: ')
        email = input('Введите Ваш e-mail: ')
        number = input('Введите Ваш телефон: ')
        return name, surname, year, city, email, number


    print(my_doc(name = 'Даниил', surname = 'Селезнёв', year = 1994, city = 'Екатеринбург', email = 'danil_king@mail.ru', number = '89995657039'))
