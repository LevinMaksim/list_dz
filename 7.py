import random

a = [random.randint(1, 100) for _ in range(10)]

min_i = a.index(min(a))
max_i = a.index(max(a))

print(a)

a[min_i], a[max_i] = a[max_i], a[min_i]

print(a)
