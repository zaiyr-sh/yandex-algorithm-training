# 1. Префиксные суммы

# Реализация RSQ (Range Sum Query) через перфиксные суммы

def make_prefix_sum(nums):
    prefix_sum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
    return prefix_sum

def rsq(prefix_sum, l, r):
    return prefix_sum[r] - prefix_sum[l]

arr = [4, 3, 2, 6, 10, 0, 3, 5, 2, 9, 7]
print(make_prefix_sum(arr))
print(rsq(make_prefix_sum(arr), 2, 5))