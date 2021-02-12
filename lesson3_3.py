def my_f(args_1,args_2,args_3):
    int(args_1)
    int(args_2)
    int(args_3)
    if min(args_1,args_2,args_3) == args_1:
        return args_3 + args_2
    if min(args_1,args_2,args_3) == args_2:
        return args_1 + args_3
    else:
        return args_1 + args_2
print(my_f(3,1,5))