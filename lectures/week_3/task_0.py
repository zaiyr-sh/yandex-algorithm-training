# Множество

# F(x) = x % setSize ==> ХЕШ-ФУНКЦИЯ
# mySet (список списков) ==> ХЕШ-ТАБЛИЦА
# Совпадение значений хеш-функции для разных параметров ==> КОЛЛИЗИЯ

setSize = 10 # размер множества
mySet = [[] for _ in range(setSize)] 

def add(x):
    if find(x):
        return "Already exists"
    mySet[x % setSize].append(x)

def find(x):
    for now in mySet[x % setSize]:
        if now == x:
            return True
    return False

def delete(x):
    xList = mySet[x % setSize]
    for i in range(len(xList)):
        if xList[i] == x:
            # xList[i], xList[len(xList) - 1] = xList[len(xList) - 1], xList[i]
            xList[i] = xList[len(xList) - 1]
            xList.pop()
            return
    return "Not found"
            
