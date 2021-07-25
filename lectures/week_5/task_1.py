# 1. Префиксные суммы

# Задача
# Дана последовательность чисел длинной N и M запросов

# Запросы: "Сколько нулей на полуинтервали [L, R)".

# Решение №1
# Для каждого запроса перебираем все числа от L до R 
# (не включительно) и считаем количество нулей. В худшем 
# случае каждый запрос за O(N)

def count_zeros(nums, l, r):
    cnt = 0
    for i in range(l, r):
        if nums[i] == 0:
            cnt += 1
    return cnt

print(count_zeros([0, 1, 3, 0, 0, 4, 0, 5, 6, 0], 0, 5))

# Time Complexity: O(NM)

# ------------------------------------------------------------------

# Решение №2
# Для каждого префикса посчитаем количества нулей на нём 
# (prefixzeros). Тогда ответ на запрос на полуинтервале [L, R): 
# prefixzeros[R] - prefixzeros[L]

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

# Time Complexity: O(N + M)