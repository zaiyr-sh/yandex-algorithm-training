# 1. Сортировка событий

# Задача
# Сайт посетило N человек, для каждого известно время входа на сайт 
# In_i, и время выхода с сайта Out_i. Считается, что человек был на сайте 
# с момента In_i, по Out_i, включительно

# Определите, каково максимальное количество человек было на сайте 
# одновременно.

# Решение
# Создадим на каждого человека два события: вход и выход. 
# Каждое событие — пара, в которой первое число — время, 
# а второе — тип события.
# «Событие «вход на сайт» должно происходить раньше «выхода с сайта»

def max_visitors_online(n, t_in, t_out):
    events = []
    for i in range(n):
        events.append((t_in[i], -1))
        events.append((t_out[i], 1))
    events.sort()
    online = 0
    max_online = 0
    for event in events:
        if event[1] == -1:
            online += 1
        else:
            online -= 1
        max_online = max(online, max_online)
    return max_online

n = 5
t_in = [5.00, 2.00, 10.00, 1.00, 7.00]
t_out = [8.00, 10.00, 12.00, 9.00, 14.00]
print(max_visitors_online(n, t_in, t_out))