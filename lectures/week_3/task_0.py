# 1. Как устроено множество?

# F(x) = x % set_size ==> ХЕШ-ФУНКЦИЯ
# my_set (список списков) ==> ХЕШ-ТАБЛИЦА
# Совпадение значений хеш-функции для разных параметров ==> КОЛЛИЗИЯ

set_size = 10 # размер множества
my_set = [[] for _ in range(set_size)] 

def add(x):
    if find(x):
        return "Already exists"
    my_set[x % set_size].append(x)

def find(x):
    for now in my_set[x % set_size]:
        if now == x:
            return True
    return False

def delete(x):
    x_list = my_set[x % set_size]
    for i in range(len(x_list)):
        if x_list[i] == x:
            # x_list[i], x_list[len(x_list) - 1] = x_list[len(x_list) - 1], x_list[i]
            x_list[i] = x_list[len(x_list) - 1]
            x_list.pop()
            return
    return "Not found"