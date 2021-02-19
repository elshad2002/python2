  f.write(f"{' '.join([str(i) for i in range(1, 21)])}")

with open("text_5.txt", "r", encoding="utf-8") as f:
    numbers = [int(i) for i in f.read().split()]
    print(sum(numbers))
