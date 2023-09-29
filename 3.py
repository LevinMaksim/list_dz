import random

num = [random.randint(1, 101) for _ in range(10)]

a = random.randint(1, 101)

if a in num:
  print(num.index(a))
else:
    print('-1')
