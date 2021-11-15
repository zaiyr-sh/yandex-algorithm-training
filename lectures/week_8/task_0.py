# 1. Собственный менеджер памяти

# Код менеджера памяти

# Инициализацмя памяти
def init_memory(max_n):
    memory = []
    for i in range(max_n):
        memory.append([0, i + 1, 0])
    return [memory, 0]

# Создать новый node
def new_node(mem_struct):
    memory, first_free = mem_struct
    mem_struct[1] = memory[first_free][1]
    return first_free

# Удалить node
def del_node(mems_truct, index):
    memory, first_free = mems_truct
    memory[index][1] = first_free
    mems_truct[1] = index

# memory = init_memory(10)
# print(memory)

# print(new_node(memory))
# print(new_node(memory))
# print(new_node(memory))
# print(memory)

# del_node(memory, 1)
# print(memory)

# print(new_node(memory))
# print(new_node(memory))
# print(new_node(memory))
# print(memory)