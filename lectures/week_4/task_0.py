# 1. Сортировка подсчетом

# Задача
# Пусть необходимо отсортировать массив из N целых чисел,
# каждое от 0 до K

# Обычная сортировка займет O(N logN)

# Данная сортировка пойдет для маленьких чисел
# и займет O(N+K) и O(K) дополнительной памяти

def count_sort(seq):
    min_val = min(seq)
    max_val = max(seq)
    k = (max_val - min_val + 1)
    count_arr = [0] * k
    for now in seq:
        count_arr[now - min_val] += 1
    now_pos = 0
    for val in range(0, k):
        for i in range(count_arr[val]):
            seq[now_pos] = val + min_val
            now_pos += 1
    return seq

print(count_sort([4,4,3,5,4,5,3,2,5,3,4,4]))