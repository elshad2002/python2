def my_f(x,y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print("error")
    if x <= 0 or y >= 0:
        print("error")
    result = 1
    for i in range(abs(y)):
        result /= x
    return round(result,5)
print(my_f(input("enter number 1:"),input("enter number 2:")))

