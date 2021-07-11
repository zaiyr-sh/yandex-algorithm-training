# Словарь. Задел под оптимизацию.

# Сгруппировать слова по общим буквам
# Sample Input: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
# Sample Output: [['eat', 'tea', 'ate'], ['nat', 'tan'], ['bat']]

def group_words(words):
    def key_by_word(word):
        # return ''.join(sorted(word))
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
