# 1. Бинарный поиск

# Всё плохо ... Всё хорошо
def l_bin_search(l, r, check, check_params):
   while l < r:
       m = (l + r) // 2
       if check(m, check_params):
           r = m
       else:
           l = m + 1
   return l

# Всё хорошо ... Всё плохо
def r_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, check_params):
            l = m
        else:
            r = m - 1
    return l

def check_is_eq(index, params):
    seq, x = params
    return seq[index] == x

seq = [1, 2, 2, 3, 4, 5, 5, 5, 7, 9, 10]
print(l_bin_search(0, 11, check_is_eq, (seq, 5)))
print(r_bin_search(0, 11, check_is_eq, (seq, 5)))