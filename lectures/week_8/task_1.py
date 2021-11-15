# 2. Бинарное дерево поиска

# Реализация поиска

import task_0 as m

def find(mem_struct, root, x):
    key = mem_struct[0][root][0]
    if x == key:
        return root
    elif x < key:
        left = mem_struct[0][root][1]
        if left == -1:
            return -1
        else:
            return find(mem_struct, left, x)
    elif x > key:
        right = mem_struct[0][root][2]
        if right == -1:
            return -1
        else:
            return find(mem_struct, right, x)

# Реализация добавления 

def create_and_fill_node(mem_struct, key):
    index = m.new_node(mem_struct)
    mem_struct[0][index][0] = key
    mem_struct[0][index][1] = -1
    mem_struct[0][index][2] = -1
    return index


def add(mem_struct, root, x):
    key = mem_struct[0][root][0]
    if x < key:
        left = mem_struct[0][root][1]
        if left == -1:
            mem_struct[0][root][1] = create_and_fill_node(mem_struct, x)
        else:
            add(mem_struct, left, x)
    elif x > key:
        right = mem_struct[0][root][2]
        if right == -1:
            mem_struct[0][root][2] = create_and_fill_node(mem_struct, x)
        else:
            add(mem_struct, right, x)


# Как создать какое-нибудь дерево?

mem_struct = m.init_memory(20)
print("mem_struct:", mem_struct)
root = create_and_fill_node(mem_struct, 8) # корень дерева
print("root:", root)
print("mem_struct:", mem_struct)
add(mem_struct, root, 9)
add(mem_struct, root, 14)
add(mem_struct, root, 13)
add(mem_struct, root, 3)
add(mem_struct, root, 1)
add(mem_struct, root, 6)
add(mem_struct, root, 4)
add(mem_struct, root, 7)
print("mem_struct:", mem_struct)
print("find(mem_struct, root, 7):", find(mem_struct, root, 7))