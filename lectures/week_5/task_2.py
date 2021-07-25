# 1. Префиксные суммы

# Дана последовательность чисел длинной N

# Необходимо найти кол-во отрезков с нулевой суммой.

# Решение №1 (Наивное решение)
# Перебираем начало и конец отрезка и просто просуммируем 
# все его элементы

def count_zeros_sum_ranges(nums):
    cnt_ranges = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            range_sum = 0
            for k in range(i, j):
                range_sum += nums[k]
            if range_sum == 0:
                cnt_ranges += 1
    return cnt_ranges

print(count_zeros_sum_ranges([-3, 2, 0, 6, 3, 5, -13]))

# Time Complexity: O(N^3)

# ------------------------------------------------------------------

# Решение №2
# Перебираем начало и будем двигать конец, суммируя элементы

def count_zeros_sum_ranges(nums):
    cnt_ranges = 0
    for i in range(len(nums)):
        range_sum = 0
        for j in range(i, len(nums)):
            range_sum += nums[j]
            if range_sum == 0:
                cnt_ranges += 1
    return cnt_ranges

print(count_zeros_sum_ranges([-3, 2, 0, 6, 3, 5, -13]))

# Time Complexity: O(N^2)

# ------------------------------------------------------------------

# Решение №3
# Насчитаем префиксные суммы. Одинаковые префиксные суммы 
# означают, что сумма на отрезке с началом и концом в позициях, 
# на которых достигаются одинаковые префиксные, 
# будет равна нулю

def count_prefix_sums(nums):
    prefix_sum_by_value = {0 : 1}
    now_sum = 0
    for now in nums:
        now_sum += now
        if now_sum not in prefix_sum_by_value:
            prefix_sum_by_value[now_sum] = 0
        prefix_sum_by_value[now_sum] += 1
    return prefix_sum_by_value

def count_zeros_sum_ranges2(prefix_sum_by_value):
    cnt_ranges = 0
    for now_sum in prefix_sum_by_value:
        cnt_sum = prefix_sum_by_value[now_sum]
        cnt_ranges += cnt_sum * (cnt_sum - 1) // 2
    return cnt_ranges

sums = count_prefix_sums([-3, 2, 0, 6, 3, 5, -13])

print(sums)
print(count_zeros_sum_ranges2(sums))

# Time Complexity: O(N)