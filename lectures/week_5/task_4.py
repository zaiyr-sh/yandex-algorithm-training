# 2. Два указателя

# Задача
# Игрок в футбол обладает одной числовой характеристикой — 
# профеосионализмом. Команда называется сплоченной, если 
# профессионализм любого игрока не превосходит суммарный 
# профессионализм любых двум других игроков из команды. 
# Команда может состоять из любого количества игроков. 
# Дана отсортированная последовательность чисел длиной N - 
# профеосионалиэм игроков

# Необходимо найти максимальный суммарный профессионализм 
# сплоченной команды.

# Решение
# Два указателя

def best_team_sum(players):
    best_sum = 0
    now_sum = 0
    last = 0
    for first in range(len(players)):
        while last < len(players) and (last == first or players[first] + players[first + 1] >= players[last]):
            now_sum += players[last]
            last += 1
        best_sum = max(best_sum, now_sum)
        now_sum -= players[first]
    return best_sum

print(best_team_sum([1, 1, 2, 4, 6, 11]))