sorts = []
with open('ice2.txt', 'r') as file:
    for line in file:
        sorts.append(line)

producers = []
producers_count = 1
for sort in sorts:
    producer = sort.split()[0]  # Получаем производителя из названия сорта
    if producer not in producers:
        producers.append(producer)
    else:
        producers = []
        producers.append(producer)
        producers_count += 1

print(producers_count)  # Выводим количество производителей


    

