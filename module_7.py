proceeds = int(input("Введите значение выручки в рублях:"))
costs = int(input("Введите значение издержек в рублях:"))
if proceeds > costs:
    print("Вы отработали  прибылью")
    profitability = proceeds / costs
    print(f"{profitability:.2f}")
    human = int(input("Введите количество сотрудников:"))
    print(f"{proceeds/human:.2f} - Прибыль фирмы в расчете на одного сотрудника")
else:
    print("Вы работаете в убыток")
