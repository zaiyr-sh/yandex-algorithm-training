# 1. Сложность

# Задача
# Дана строка (в кодировке UTF-8)

# Найти самый часто встречающийся в ней символ.
# Если несколько символов встречаются одинаково
# часто, то можно вывести любой.

# Решение №1
# Перебираем все позиции и для каждой позиции в строке еще раз 
# переберем все позиции и случае совпадения прибавим к счетчику 
# единицу. Найдем максимальне значение счётчика

s = "ababa"
ans = ''
anscnt = 0
for i in range(len(s)):
    nowcnt = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            nowcnt += 1
    if nowcnt > anscnt:
        ans = s[i]
        anscnt = nowcnt
print('Решение №1:', ans)

# Time Complexity: O(N^2)
# Memory Complexity: O(N)

# ------------------------------------------------------------------

# Решение №2
# Перебираем все символы, встречающиеся в строке, а затем переберем 
# все позиции и в случае совпадения прибавим к счетчику единицу. 
# Найдем максимальне значение счётчика

s = "ababa"
ans = ''
anscnt = 0
for now in set(s):
    nowcnt = 0
    for j in range(len(s)):
        if now == s[j]:
            nowcnt += 1
    if nowcnt > anscnt:
        ans = now
        anscnt = nowcnt
print('Решение №2:', ans)


# Time Complexity: O(NK)
# Memory Complexity: O(N)
# K - кол-во различных букв

# ------------------------------------------------------------------

# Решение №3
# Заведём словарь, где ключом является символ, а значение — сколько 
# раз он встретился. Если символ встретился впервые — создаем 
# элемент словаря с ключом, совпадающим с этим символом 
# и значением ноль. Прибавляем к элементу словаря с ключом, 
# совпадающем с этим символом, единицу.

s = "ababa"
ans = ''
anscnt = 0
dct = {}
for now in s:
    if now not in dct:
        dct[now] = 0
    dct[now] += 1
for key in dct:
    if dct[key] > anscnt:
        ans = key
        anscnt = dct[key]
print('Решение №3:', ans)

# Time Complexity: O(N + K) = O(N)
# Memory Complexity: O(K)