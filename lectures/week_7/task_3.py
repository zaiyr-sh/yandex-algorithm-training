# 1. Сортировка событий

# Задача
# Сайт посетило N человек, для каждого известно время входа на сайт 
# In_i, и время выхода с сайта Out_i. Считается, что человек был на сайте 
# с момента In_i, по Out_i, включительно. Начальник заходил на сайт M раз 
# в моменты времени Boss_i и смотрел, сколько людей сейчас онлайн. 
# Посещения сайта начальником упорядочены по возрастанию 
# времени

# Определите, какие показания счётчика людей онлайн увидел начальник.

# Решение
# Создадим третий тип события — «вход начальника» и при наступлении 
# такого события будем сохранять текущее значение счетчика посетителей

def boss_counters(n, t_in, t_out, m, t_boss):
    events = []
    for i in range(n):
        events.append((t_in[i], -1))
        events.append((t_out[i], 1))
    for i in range(m):
        events.append((t_boss[i], 0))
    events.sort()
    online = 0
    boss_ans = []
    for i in range(len(events)):
        if events[i][1] == -1:
            online += 1
        elif events[i][1] == 1:
            online -= 1
        else:
            boss_ans.append(online)
    return boss_ans

n = 4
t_in = [8.00, 9.00, 12.00, 18.00]
t_out = [11.00, 12.00, 15.00, 20.00]
m = 2
t_boss = [12.00, 20.00]
print(boss_counters(n, t_in, t_out, m, t_boss))