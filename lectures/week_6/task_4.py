# 1. Бинарный поиск

# Задача
# Задана отсортированная по неубыванию последовательность 
# из N чисел и число X

# Необходимо определить индекс первого числа в последовательности, 
# которое больше либо равно X. Если такого числа нет, то вернуть число N.

# Решение
# Воспользуемся левым бинпоиском для поиска первого подходящего 
# числа. В случае, если бинпоиск сошелся к числу, меньшему X вернём N

def check_is_ge(index, params):
   seq, x = params
   return seq[index] >= x

def find_first_ge(seq, x):
   ans = l_bin_search(0, len(seq) - 1, check_is_ge, (seq, x))
   if seq[ans] < x:
       return len(seq)
   return ans

def l_bin_search(l, r, check, check_params):
   while l < r:
       m = (l + r) // 2
       if check(m, check_params):
           r = m
       else:
           l = m + 1
   return l

print(find_first_ge([1, 2, 2, 3, 4, 5, 5, 7, 9, 10], 4))