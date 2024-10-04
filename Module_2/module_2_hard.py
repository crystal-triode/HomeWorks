import random

n = random.randint(3, 20)
pairs = []

for a in range(1, n):
    for b in range(1, n):
        if b >= a:
            continue
        s = a + b
        if n % s == 0:
            pairs.append((a, b))
print("Случайное число : ", n)
print("Подходящие пары: ", pairs)