def maximum_non_overlapping_intervals(intervals):
    # Сортируем интервалы по времени окончания
    intervals.sort(key=lambda x: x[1])
    
    # Инициализируем текущий интервал и счетчик
    current_interval = intervals[0]
    count = 1
    
    # Проходим по остальным интервалам
    for interval in intervals[1:]:
        # Если начало интервала не меньше времени окончания текущего интервала,
        # то добавляем интервал в список непересекающихся интервалов и
        # обновляем текущий интервал
        if interval[0] >= current_interval[1]:
            count += 1
            current_interval = interval
    
    # Возвращаем количество непересекающихся интервалов
    return count

# генерируем список заявок
requests = []
with open('request2.txt', 'r') as file:
    n = int(file.readline())
    for line in file:
        start_time, finish_time = map(int, line.split())
        requests.append((start_time, finish_time))

print(maximum_non_overlapping_intervals(requests))

