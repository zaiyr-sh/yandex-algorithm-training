# 3. Два прохода

# Задача
# На парковке в торговом центре N мест (занумерованных от 1 до N). 
# За день в ТЦ приезжало М автомобилей, при этом некоторые из них 
# длинные и занимали несколько подряд идущих парковочных мест. 
# Для каждого автомобиля известно время приезда и отъезда, а также 
# два числа — с какого по какое парковочные места он занимал. 
# Если в какай-то момент времени один автомобиль уехал 
# с парковочного места, то место считается освободившимся 
# и в тот же момент времени на его места может встать другой

# Необходимо определить, был ли момент, в который были заняты все 
# парковочные места и определить минимальное количество автомобилей, 
# которое заняло все места, а также номера этих автомобилей 
# (в том порядке, как они перечисляются в списке). Если парковка 
# никогда не была занята полностью вернуть пустой список.

# Решение (неэффективное)
# Добавим в событие номер автомобиля в списке. При обновлении 
# минимума просто копируем текущее состояние в ответ

def min_cars_on_full_parking(cars, n):
    events = []
    for i in range(len(cars)):
        time_in, time_out, place_from, place_to = cars[i]
        events.append((time_in, 1, place_to - place_from + 1, i))
        events.append((time_out, -1, place_to - place_from + 1, i))
    events.sort()
    occupied = 0
    now_cars = 0
    min_cars = len(cars) + 1
    car_nums = set()
    best_car_nums = set()
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            now_cars -= 1
            car_nums.remove(events[i][3])
        elif events[i][1] == 1:
            occupied += events[i][2]
            now_cars += 1
            car_nums.add(events[i][3])
        if occupied == n and now_cars < min_cars:
            best_car_nums = car_nums.copy()
            min_cars = now_cars
    return sorted(best_car_nums)

cars = (
        [13.00, 20.00, 1, 1],
        [12.00, 17.00, 2, 3],
        [12.00, 15.00, 4, 7],
        [16.00, 17.00, 4, 7],
        [15.00, 19.00, 8, 9],
        [14.00, 16.00, 10, 10],
        [16.00, 18.00, 10, 10],
    )
n = 10
print(min_cars_on_full_parking(cars, n))

# Time Complexity: M^2 / 3

# ------------------------------------------------------------------

# Решение (эффективное)

def min_cars_on_full_parking(cars, n):
    events = []
    for i in range(len(cars)):
        time_in, time_out, place_from, place_to = cars[i]
        events.append((time_in, 1, place_to - place_from + 1, i))
        events.append((time_out, -1, place_to - place_from + 1, i))
    events.sort()
    occupied = 0
    now_cars = 0
    min_cars = len(cars) + 1
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            now_cars -= 1
        elif events[i][1] == 1:
            occupied += events[i][2]
            now_cars += 1
        if occupied == n and now_cars < min_cars: 
            min_cars = now_cars
    car_nums = set()
    now_cars = 0
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            now_cars -= 1
            car_nums.remove(events[i][3])
        elif events[i][1] == 1:
            occupied += events[i][2]
            now_cars += 1
            car_nums.add(events[i][3])
        if occupied == n and now_cars == min_cars:
            return sorted(car_nums)
    return set()

cars = (
        [13.00, 20.00, 1, 1],
        [12.00, 17.00, 2, 3],
        [12.00, 15.00, 4, 7],
        [16.00, 17.00, 4, 7],
        [15.00, 19.00, 8, 9],
        [14.00, 16.00, 10, 10],
        [16.00, 18.00, 10, 10],
    )
n = 10
print(min_cars_on_full_parking(cars, n))

# Time Complexity: M * logM