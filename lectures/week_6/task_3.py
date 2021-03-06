# 1. Бинарный поиск

# Задача
# Михаил читает лекции по алгоритмам. За кадром стоит доска 
# размером W * Н сантиметров. Михаилу нужно разместить на доске 
# N квадратных стикеров со шпаргалками, при этом длина стороны 
# стикера в сантиметрах должна быть целым числом

# Определите максимальную длину стороны стикера, чтобы все стикеры 
# поместились на доске.

# Решение
# Будем искать максимальную сторону стикера бинарным поиском

def r_bin_search(l, r, check, check_params):
    while l != r:
        m = (l + r + 1) // 2
        if check(m, check_params):
            l = m
        else:
            r = m - 1
    return l


def check_stickers(size, params):
    n, w, h = params
    return (w // size) * (h // size) >= n


l = 0
n = 10
w = 100
h = 100
print(r_bin_search(l, n, check_stickers, [n, w, h]))