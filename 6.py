import random

a = [random.randint(1, 100) for _ in range(10)]

for i in a:
    if a.count(i) > 1:
        print(i)
