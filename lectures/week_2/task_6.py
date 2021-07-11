# Два прохода

# Дана последовательность слов
# Вывести все самые короткие слова через пробел

def shortWords(words):
    minLen = len(words[0])
    for word in words:
        if len(word) < minLen:
            minLen = len(word)
    ans = []
    for word in words:
        if len(word) == minLen:
            ans.append(word)
    return " ".join(ans)

print(shortWords(["aaa", "b", "cc", "dddd", "e", "f"]))
