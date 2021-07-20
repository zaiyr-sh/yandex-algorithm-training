# 1. Как устроено множество?

# Задача
# Дан словарь из N слов, длина каждого не превосходит K

# В записи каждого из M слов текста (каждое длиной до K)
# может быть пропущена одна буква. Для каждого слова
# сказать, входит ли оно (возможно, с одной пропущенной
# буквой), в словарь

# Решение
# Выбросим из каждого слова словаря по одной букве всеми 
# возможными способами за O(NK) и положим получившиеся 
# слова в множество.

# Для каждого слова из текста проверим, есть ли оно 
# в словаре за O(1)

def wordsInDict(dictionary, text):
    goodWords = set(dictionary)
    for word in dictionary:
        for delPos in range(len(word)):
            goodWords.add(word[:delPos] + word[delPos+1:])
    ans = []
    for word in text:
        ans.append(word in goodWords)
    return ans

print(wordsInDict(["hello"], ["helo", "world", "ello", "my", "friends"]))

# Time Complexity: O(NK^2 + M)