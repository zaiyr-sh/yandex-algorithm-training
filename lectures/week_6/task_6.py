# 2. Задача из жизни

# Задача 
# Задана процентная ставка по кредиту (X% годовых), срок 
# кредитования (N месяцев) и сумма кредита (M рублей)

# Необходимо рассчитать размер аннуетиного платежа ежемесячного платежа 
# (платеж одинаковой суммы каждый месяц)

# Решение подзадачи о ежемесячном проценте
# Ежемесячный процент не равен X/12! Подберем его бинпоиском.
# Бинпоиск для вещественных чисел

def check_monthly_paid(m_perc, y_perc):
    m_sum = 1 + m_perc / 100
    y_sum = 1 + y_perc / 100
    return m_sum ** 12 >= y_sum

    
def f_bin_search(l, r, eps, check, check_params):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, check_params):
            r = m
        else:
            l = m + 1
    return l


x = 12
eps = 0.0001
m_perc = f_bin_search(0, x, eps, check_monthly_paid, x)
print(m_perc)

# Решение задачи о размере платежа
# Будем перебирать сумму платежа бинпоиском, а в качестве проверки
# моделировать процесс ежемесячной выплаты, уменьшая тело кредита
# на разницу между суммой платежа и ежемесячным процентом

def check_credit(m_pay, params):
    periods, credit_sum, m_perc = params
    for i in range(periods):
        percpay = credit_sum * (m_perc / 100)
        credit_sum  -= m_pay - percpay
    return credit_sum <= 0


def f_bin_search(l, r, eps, check, check_params):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, check_params):
            r = m
        else:
            l = m + 1
    return l

eps = 0.01
m = 10000000
n = 300
monthlypay = f_bin_search(0, m, eps, check_credit, (n, m, m_perc))
print(monthlypay)