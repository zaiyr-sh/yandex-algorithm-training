# 2. Словари

# Задача
# Дана строка S

# Выведите гистограмму как в примере (коды символов 
# отсортированы)

# S = Hello, World!

#       #
#       ##
# ##########
#  !,Hdelorw

# Решение
# Для каждого символа в словаре посчитаем, сколько раз он встречался.
# Найдем самый частый и переберем количество от этого числа 
# до 1. Пройдём по всем отсортированным ключам и если количество 
# больше счётчика — выведем #

def print_chart(s):
    sym_count = {}
    max_sym_count = 0
    for sym in s:
        if sym not in sym_count:
            sym_count[sym] = 0
        sym_count[sym] += 1
        max_sym_count = max(max_sym_count, sym_count[sym])
    sorted_uniq_syms = sorted(sym_count.keys())
    for row in range(max_sym_count, 0, -1):
        for sym in sorted_uniq_syms:
            if sym_count[sym] >= row:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print(''.join(sorted_uniq_syms))

print_chart('Hello, World!')