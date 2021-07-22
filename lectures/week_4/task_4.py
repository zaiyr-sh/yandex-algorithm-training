# 3. Задел под оптимизацию.

# Задача
# Сгруппировать слова по общим буквам
# Sample Input: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
# Sample Output: [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]

# Решение здорового человека
# Отсортируем в каждом слове буквы и это будет выступать в роли 
# ключа, а значение будет список слов

def group_words(words):
    groups = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in groups:
            groups[sorted_word] = []
        groups[sorted_word].append(word)
    ans = []
    for sorted_word in groups:
        ans.append(groups[sorted_word])
    return ans

print(group_words(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))

# ------------------------------------------------------------------

# Подозрения здорового человека
# sortedword = ''.join(sorted(word))
# Вдруг слово будет длинное (N)? Сортировка займет O(N logN). 
# Количество различных букв в слове K <= N, можем посчитать количество 
# каждой за O(N) и отсортировать за O(K logK), теоритически

# ------------------------------------------------------------------

# Задел здорового человека
# Будет тормозить - посмотрим на профилировщике где, и если долго 
# считается ключ - легко поправим на что-то более эффективное

def group_words(words):
    def key_by_word(word):
        return ''.join(sorted(word))
            
    groups = {}
    for word in words:
        sorted_word = key_by_word(word)
        if sorted_word not in groups:
            groups[sorted_word] = []
        groups[sorted_word].append(word)
    ans = []
    for sorted_word in groups:
        ans.append(groups[sorted_word])
    return ans

print(group_words(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))

# ------------------------------------------------------------------

# Оптимизация (?) здорового человека

def group_words(words):
    def key_by_word(word):
        syms = {}
        for sym in word:
            if sym not in syms:
                syms[sym] = 0
            syms[sym] += 1
        lst = []
        for sym in sorted(syms.keys()):
            lst.append(sym)
            lst.append(str(syms[sym]))
        return ''.join(lst)
                
    groups = {}
    for word in words:
        sorted_word = key_by_word(word)
        if sorted_word not in groups:
            groups[sorted_word] = []
        groups[sorted_word].append(word)
    ans = []
    for sorted_word in groups:
        ans.append(groups[sorted_word])
    return ans

print(group_words(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))