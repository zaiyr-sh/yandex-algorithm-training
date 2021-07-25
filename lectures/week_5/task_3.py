# 2. Два указателя

# Задача

# Дана отсортированная последовательность чисел 
# длинной N и число K

# Необходимо найти количество пар A, B, таких что B - A > K.

# Решение №1
# Перебираем все пары чисел и для каждой проверим условие

def cnt_pairs_with_diff_gtk(sorted_nums, k):
    cnt_pairs = 0
    for first in range(len(sorted_nums)):
        for last in range(first, len(sorted_nums)):
            if sorted_nums[last] - sorted_nums[first] > k:
                cnt_pairs += 1
    return cnt_pairs

print(cnt_pairs_with_diff_gtk([1, 3, 5, 7, 8], 4))    

# Time Complexity: O(N^2)

# ------------------------------------------------------------------

# Решение №2
# Возьмем наименьшее число и найдем для него первое подходящее 
# большее. Все ещё большие числа точно подходят. Возьмем в качестве 
# меньшего числа следующее, а указатель первого подходящего 
# большего будем двигать начиная с той позиции, где он находится 
# сейчас

def cnt_pairs_with_diff_gtk(sorted_nums, k):
    cnt_pairs = 0
    last = 0
    for first in range(len(sorted_nums)):
        while last < len(sorted_nums) and sorted_nums[last] - sorted_nums[first] <= k:
            last += 1
        cnt_pairs += len(sorted_nums) - last
    return cnt_pairs

print(cnt_pairs_with_diff_gtk([1, 3, 5, 7, 8], 4))    

# Time Complexity: O(N)