month = int(input("Enter month: ")
d = {1: [12,1,2], 2: [3,4,5], 3: [6,7,8], 4: [9,10,11]}
if month in d[1]:
    print("Ваш месяц относится к зиме")
elif month in d[2]:
    print("Ваш месяц относится к весне")
elif month in d[3]:
    print("Ваш месяц относится к лету")
elif month in d[4]:
    print("Ваш месяц относится к осени")
else:
    print("Error")