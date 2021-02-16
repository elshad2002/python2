from itertools import count, cycle
for el in count(10):
    if el > 18:
        break
    print(el)
my_list = [1, 2, 5, 675, 767,13]
c = 0
for i in cycle(my_list):
    if c > 15:
        break
    print(i)
    c += 1