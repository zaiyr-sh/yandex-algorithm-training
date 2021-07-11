# Префиксные суммы

# Дана последовательность чисел длинной N
# Необходимо найти кол-во отрезков с нулевой суммой.

# Решение за O(N^2)

def count_zeros_sum_ranges(nums):
    cnt_ranges = 0
    for i in range(len(nums)):
        range_sum = 0
        for j in range(i, len(nums)):
            range_sum += nums[i]
            if range_sum == 0:
                cnt_ranges += 1
    return cnt_ranges

print(count_zeros_sum_ranges([-3, 2, 0, 6, 3, 5, 0]))

# Решение за O(N)

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
        cnt_ranges += cnt_sum * (cnt_sum - 1) # 2
    return cnt_ranges

sums = count_prefix_sums([-3, 2, 0, 6, 3, 5, 0])

print(sums)
print(count_zeros_sum_ranges2(sums))

        

