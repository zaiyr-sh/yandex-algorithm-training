# Задача с собеседования

# Дана строка, состоящая из букв A-Z:
# "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# "A4B3C2XYZD4E3F3A6B28". И сгенерирует любую ошибку, если на вход
# пришла невалидная строка.
# Пояснение:
# 1. если символ встречается 1 раз, он остается без изменений
# 2. если символ повторяется более 1 раза,
# к нему добавляется количество повторений

def rle(s):
    def pack(s, cnt):
        if cnt > 1:
            return s + str(cnt)
        return s
    
    lastSym = s[0]
    lastPos = 0
    ans = []
    for i in range(1, len(s)):
        if s[i] != lastSym:
            ans.append(pack(lastSym, i - lastPos))
            lastPos = i
            lastSym = s[i]
    ans.append(pack(s[lastPos], len(s) - lastPos))
    return ''.join(ans)

print(rle(['a', 'a', 'b', 'b', 'c', 'a']))
