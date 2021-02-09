my_str = input("Введите строку из нескольких слов через пробел").split()
for i, word in enumerate(my_str, 1):
    print(f"{i} {word[:10]}")