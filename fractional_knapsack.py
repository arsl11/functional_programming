class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def fractional_knapsack(capacity, items):
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_value = 0
    for item in items:
        if capacity == 0:
            return total_value
        elif item.weight <= capacity:
            capacity -= item.weight
            total_value += item.value
        else:
            fraction = capacity / item.weight
            total_value += item.value * fraction
            capacity = 0
    return total_value

# чтение предметов из файла
items = []
with open('cont2.txt', 'r') as file:
    for line in file:
        weight, value = map(int, line.split())
        items.append(Item(weight, value))

capacity = 100000
max_value = fractional_knapsack(capacity, items)
print("Максимальная стоимость:", max_value)

# В этом примере мы создаем класс Item, который хранит информацию о весе и стоимости предмета, а также о соотношении стоимости к весу. 
# Затем мы сортируем список предметов по этому соотношению в порядке убывания итерируемся по ним, добавляя предметы в рюкзак, 
# пока его вместимость не будет исчерпана. Если следующий предмет не помещается целиком в рюкзак, 
# мы добавляем только долю предмета, которая помещается в оставшееся место.