my_list = [56, 3435, 1, 79, 14, 2, 2, 69, 88, 17, 1020, 7]
new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")
