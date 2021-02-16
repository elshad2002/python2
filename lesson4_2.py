my_list = [3, 4, 1, 66, 15, 245, 360, 20, 8, 18]
new_list = [my_list[num] for num in range(1,len(my_list)) if my_list[num] > my_list[num - 1]]
print(my_list)
print(new_list)
