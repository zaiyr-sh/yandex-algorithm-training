# 3. Тернарный поиск (которого нет)

# Задача 
# Велосипедисты, участвующие в шоссейной гонке, в некоторый момент 
# времени, который называется начальным, оказались в точках, 
# удаленных от места старта на x1, x2, ..., хn метров (n - общее количество 
# велосипедистов, не превосходит 100 000). Каждый велосипедист 
# двигается со своей постоянной скоростью v1, v2, ..., vn метров в секунду. 
# Все велосипедисты двигаются в одну и ту же сторону. 
# Репортер, освещающий ход соревнований, хочет определить момент 
# времени, в который расстояние между лидирующим в гонке 
# велосипедистом и замыкающим гонку велосипедистом станет 
# минимальным, чтобы с вертолета сфотографировать сразу всех 
# участников велогонки

# Решение
# Определим функцию dist(t), которая будет за O(N) определять 
# расстояние между лидером и замыкающим в момент времени t. 
# Если dist(t + ε) > dist(t), то функция растёт и надо сдвинуть левую 
# границу поиска, иначе — правую

def dist(t, params):
    x, v = params
    min_pos = max_pos = x[0] + v[0] * t
    for i in range(1,len(x)):
        nowpos = x[i] + v[i] * t
        min_pos = min(min_pos, nowpos)
        max_pos = max(max_pos, nowpos)
    return max_pos - min_pos

def check_asc(t, eps, params):
    return dist(t + eps, params) >= dist(t, params)

def f_bin_search(l, r, eps, check, params):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, eps, params):
            r = m
        else:
            l = m
    return l

l = 0
r = 100
eps = 0.0001
print(f_bin_search(l, r, eps, check_asc, (eps, [1,2,2,2,3,4,5,6,6,7,8,9,10])))