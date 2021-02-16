from itertools import count
from math import factorial
def fact_gen():
    for el in count(1):
        yield factorial(el)
generator = fact_gen()
x = 0
for el in generator:
    if x ==15:
        break
    else:
        x += 1
        print(f"Factorial {x} = {i}")
