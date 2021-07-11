# Классические задачи линейного поиска O(n)

# Дана последовательность чисел длиной N (N > 0)
# Найти максимальное число X в последовательности

def findMax(seq):
    ans = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > ans:
            ans = seq[i]
    return ans

print(findMax([6, 2, 1, 3, 7, 3, 10, 3, 2, 5, 2]))
