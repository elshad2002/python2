my_list = [1, 1, 1, 2, 3, 3, 3, 56, 77, 77, 32, 2, 84]
new_list = [el for el in my_list if my_list.count(el) == 1 ]
print(new_list)