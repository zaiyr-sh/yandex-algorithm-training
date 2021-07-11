# 2. Особые случаи

# Решение №3 (модифицированное)

s = "ababa"
# ans = '' для пустой строки вызовется Runtime Error
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

# ------------------------------------------------------------------

# Сумма последовательности

seq = [5, 2, 1, 3, 4]

# Решение

if len(seq) == 0:
    print(0)
else:
    seqsum = seq[0]
    for i in range(1, len(seq)):
        seqsum += seq[i]
    print('Sequence Sum №1:', seqsum)

# Улучшенное решение

seqsum = 0
for i in range(len(seq)):
    seqsum += seq[i]
print('Sequence Sum №2:', seqsum)

# ------------------------------------------------------------------

# Максимум последовательности

seq = [-5, -2, -1, -3, -4]

# Решение

seqmax = 0
for i in range(len(seq)):
    if seq[i] > seqmax:
        seqmax = seq[i]
print('Maximum Consistency №1:', seqmax)

# Улучшенное решение

if len(seq) == 0:
    print('-inf')
else:
    seqmax = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > seqmax:
            seqmax = seq[i]
    print('Maximum Consistency №2:', seqmax)