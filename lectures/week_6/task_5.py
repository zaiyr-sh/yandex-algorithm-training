# 1. Бинарный поиск

# Задача
# Задана отсортированная по неубыванию последовательность 
# из N чисел и число X

# Необходимо определить сколько раз число X входит 
# в последовательность.

# Решение
# Найдем одним левым бинпоиском правое число большее либо равное X, 
# а вторым левым бинпоиском — число строго большее X. 
# Разность индексов и будет количеством вхождений

def check_is_gt(index, params):
    seq, x = params
    return seq[index] > x

def check_is_ge(index, params):
    seq, x = params
    return seq[index] >= x

def find_first(seq, x, check):
    ans = l_bins_earch(0, len(seq) - 1, check, (seq, x))
    if not check(ans, (seq, x)):
        return len(seq)
    return ans

def count_x(seq, x):
    index_gt = find_first(seq, x, check_is_gt)
    index_ge = find_first(seq, x, check_is_ge)
    return index_gt - index_ge
    
def l_bins_earch(l, r, check, check_params):
    while l < r:
        m = (l + r) // 2
        if check(m, check_params):
            r = m
        else:
            l = m + 1
    return l

print(count_x([1, 2, 2, 3, 4, 5, 5, 5, 7, 9, 10], 5))