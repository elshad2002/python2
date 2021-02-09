rating = [7,5, 3, 3, 2]
for _ in range(3):
    i = int(input())
    flag = False
    for j in range(len(rating)):
        if rating[j] < i:
            rating.insert(j, i)
            flag = True
            break
    if not flag:
        rating.append(i)
    print(rating)