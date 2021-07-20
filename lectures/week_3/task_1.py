# 1. Как устроено множество?

# Дана последовательность положительных
# чисел длинной N и число X

# Нужно найти два различных числа А и B
# из последовательности, таких что A + B = X
# или вернуть пару 0, 0, если такой пары чисел нет

# Решение №1
# Перебираем число A за O(N). Перебираем число B за O(N). 
# Если их сумма равна X, вернем эту пару
def twoTermsWithSumX(nums, x):
    for i in range(len(nums)):
        for j in range(i + i, len(nums)):
            if nums[i] + nums[j] == x:
                return nums[i], nums[j]
    return 0, 0

print(twoTermsWithSumX([1, 2, 3, 4], 5))

# Time Complexity: O(N^2)

# Решение №2
# Будем хранить все уже обработанные числа в множестве. 
# Если очередное число nownum, а X — nownum есть 
# в множестве, то мы нашли слагаемые

def twoTermsWithSumX2(nums, x):
    prevNums = set()
    for nowNum in nums:
        if x - nowNum in prevNums:
            return nowNum, x - nowNum
        prevNums.add(nowNum)
    return 0, 0

print(twoTermsWithSumX2([1, 2, 3, 4], 5))

# Time Complexity: O(N)