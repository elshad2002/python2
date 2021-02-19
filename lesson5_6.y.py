d = dict()
with open("../examples5/text_6.txt", encoding="utf-8") as f:
    for line in f:
        name, rest = line.split(':')
        rest = rest.split()
        num = 0
        for part in rest:
            if "-" in part:
                continue
            nums, type = part.split('(')
            num += int(nums)
        d[name] = num
print(d)