# Сортировка подсчетом

# Дано два числа X и Y без ведущий нулей.
# Необходимо проверить, можно ли получить первое
# из второго перестановкой цифр

def is_digit_permutation(x, y):
    def count_digits(num):
        digit_count = [0] * 10
        while num > 0:
            last_digit = num % 10
            digit_count[last_digit] += 1
            num //= 10
        return digit_count
    
    digits_x = count_digits(x)
    digits_y = count_digits(y)
    
    for digit in range(10):
        if digits_x[digit] != digits_y[digit]:
            return False
    return True

print(is_digit_permutation(2021, 1202))
print(is_digit_permutation(2021, 2202))
