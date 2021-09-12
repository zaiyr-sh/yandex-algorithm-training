# 1. Сортировка событий

# Задача
# Сайт посетило N человек, для каждого известно время входа на сайт 
# In_i, и время выхода с сайта Out_i. Считается, что человек был на сайте 
# с момента In_i, по Out_i, включительно

# Определите, какое суммарное время на сайте был хотя бы один человек.

# Решение
# Если мы пришли в событие с положительным счетчиком количества 
# людей, то между этим и предыдущим событием на сайте кто-то был. 
# Прибавим к ответу время между текущим и предыдущим событием

def time_with_visitors(n, t_in, t_out):
    events = []
    for i in range(n):
        events.append((t_in[i], -1))
        events.append((t_out[i], 1))
    events.sort()
    online = 0
    not_empty_time = 0
    for i in range(len(events)):
        if online > 0:
            not_empty_time += events[i][0] - events[i - 1][0]
        if events[i][1] == -1:
            online += 1
        else:
            online -= 1
    return not_empty_time

n = 4
t_in = [8.00, 9.00, 12.00, 18.00]
t_out = [11.00, 12.00, 15.00, 20.00]
print(time_with_visitors(n, t_in, t_out))