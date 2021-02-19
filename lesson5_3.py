with open("text_2.txt", "r", encoding="utf=8") as f:
    aver_income = 0
    names = []
    num = 0
    for line in f:
        num += 1
        name, income =(i for i in line.split())
        income = float(income)
        if income < 20000:
            names.append(name)
        aver_income += income
        aver_income = aver_income / num
print(names)
print(aver_income)

