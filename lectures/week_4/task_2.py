# 2. Словари

# Задача
# На шахматной доске N * N находятся M ладей (ладья бьет
# клетки на той же горизонтали или вертикали до ближайшей занятой)

# Опеределите, сколько пар ладей бьют друг друга.
# Ладьи задаются парой чисел I и J, обозначающих координаты клетки.
# 1 <= N <= 10^9, 0 <= M <= 2 * 10^5

# Решение
# Для каждой занятой горизонтали и вертикали будем хранить 
# количество ладей на них. Количество пар по горизонтали 
# (вертикали) равно количеству ладей минус 1. Суммируем 
# это количество пар для всех горизонталей и вертикалей.

def count_beating_rooks(rook_coords):
    rooks_in_row = {}
    rooks_in_col = {}

    def add_rook(row_or_col, key):
        if key not in row_or_col:
            row_or_col[key] = 0
        row_or_col[key] += 1

    def count_pairs(row_or_col):
        pairs = 0
        for key in row_or_col:
            pairs += row_or_col[key] - 1
        return pairs

    for row, col in rook_coords:
        add_rook(rooks_in_row, row)
        add_rook(rooks_in_col, col)
        
    return count_pairs(rooks_in_row) + count_pairs(rooks_in_col)


print(count_beating_rooks([(3, 3), (1, 1), (3, 1), (2, 2)]))
print(count_beating_rooks([(5, 2), (1, 5), (5, 1)]))