res = dict()
aver_profit = 0
num = 0
with open("../examples5/text_7.txt", encoding="utf-8") as f:
    for line in f:
        name, type, income, cost = line.split()
        profit = int(income) - int(cost)
        if profit >= 0:
            aver_profit += profit
            num += 1
        res[name] = profit
aver_profit /= num
with open("json7.json", "w", encoding="utf-8") as f:
    json.dump([res, {"average_profit": aver_profit}], f, ensure_ascii=False) 