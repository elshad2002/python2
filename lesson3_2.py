def my_f(*args):
    name = input("Enter your name:")
    surname = input("Enter your surname:")
    birthday = input("Enter your birthday:")
    town = input("Enter your town:")
    email = input("Enter your email:")
    number = input("Enter your number:")
    return f"Name-{name}, Surname-{surname},birthday-{birthday}, Town-{town},email-{email},number-{number}"
print(my_f())