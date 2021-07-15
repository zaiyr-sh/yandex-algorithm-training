import math
## 3. Покрытие тестами

# Задача 
# Даны три целых числа a, b, c. 
# Найдите все корни уравнении aх^2 * bx * c = 0 
# и выведите их в порядке возрастания

# Решение №8

a = 1
b = -2
c = 0

if a == 0:
    if b != 0:
        print(-c / b)
    if b == 0 and c == 0:
        print("Infinite number of solutions")
else:
    d = b ** 2 - 4 * a * c
    if d == 0:
        x1 = -b / (2 * a)
        print(x1)
    elif d > 0:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        if x1 < x2:
            print('Решение №8:', x1, x2)
        else:
            print('Решение №8:', x2, x1)