with open("text.txt", 'w', encoding = "utf-8") as f:
    uses_str = input()
    f.write(uses_str + '\n')
    print(uses_str,file=f)



