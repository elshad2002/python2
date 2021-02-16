from functools import reduce
gen_list = [el for el in range(100,1001) if el % 2 ==0]
def my_f(prev_arg,arg):
    return prev_arg + arg
print(reduce(my_f, gen_list))