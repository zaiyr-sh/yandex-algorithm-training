# Классические задачи линейного поиска O(n)

# Дана последовательность чисел длиной N 
# Найти минимальное четное число в последовательности
# или вывести -1, если такого не существует.

def findMinEven(seq):
    ans = -1
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (ans == -1 or seq[i] < ans):
            ans = seq[i]
    return ans

print(findMinEven([3, 5, 10, 2, 1, 6, 2, 12, 4, 8]))
