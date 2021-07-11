# Префиксные суммы

# Дана последовательность чисел длинной N и M запросов
# Запросы: "Сколько нулей на полуинтервали [L, R)".

# Решение за O(N + M)

def make_prefix_zeroes(nums):
    prefix_zeroes = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        if nums[i - 1] == 0:
            prefix_zeroes[i] = prefix_zeroes[i - 1] + 1
        else:
            prefix_zeroes[i] = prefix_zeroes[i - 1]
    return prefix_zeroes

def count_zeroes(prefix_zeroes, k, l):
    return prefix_zeroes[l] - prefix_zeroes[k]


elm = make_prefix_zeroes([0, 1, 3, 0, 0, 4, 0, 5, 6, 0])

print(elm)
print(count_zeroes(elm, 0, 5))
