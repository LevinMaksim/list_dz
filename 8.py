import random

a = int(input('Введите число: '))

b = [random.randint(1, 100) for _ in range(a)]

print(b[::2])
