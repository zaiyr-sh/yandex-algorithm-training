# Классические задачи линейного поиска O(n)

# Дана последовательность чисел длиной N
# Найти последнее (правое) вхождение числа X в нее
# или вывести -1, если число X не встречалось

def findRightX(seq, x):
    ans = -1
    for i in range(len(seq)):
        if seq[i] == x:
            ans = i
    return ans

print(findRightX([3, 2, 4, 2, 1], 2))
