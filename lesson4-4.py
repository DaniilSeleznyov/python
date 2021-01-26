my_list = [56, 88, 1, 79, 14, 2, 2, 69, 88, 17, 79, 79]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")
