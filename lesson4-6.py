from itertools import count
from itertools import cycle

i = int(input('Введите целое число, с которого начнется отсчет: '))
for el in count (i):
    if el > 60:
        break
    else:
        print(el)

print('\nДалее цикл:\n-----------------------------\n')

my_list = [True, 1313, 'Контакт']
c = 0
for em in cycle (my_list):
    if c > 20:
        break
    else:
        print(em)
        c += 1
