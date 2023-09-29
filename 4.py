import random

num = [random.randint(1, 101) for _ in range(10)]

sum = 0
a = 1

for i in num:
    sum += i
    a *= i

print(sum, a)
