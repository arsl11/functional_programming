friends = []

with open('friends2.txt', 'r') as file:
    n, m = map(int, file.readline().split())
    for line in file:
        x, y = map(int, line.split())
        friends.append([x, y])

def check(musk, seq):
    musk = list(map(int, bin(musk)[2:]))
    for i in range(len(musk)):
        a, b = musk[~i], seq[i]
        if not(not a or b):
            return False
    return True

a = [[0 if i != j else 1 for i in range(n)] for j in range(n)]

for i in range(m):
    x, y = friends[i]
    a[x - 1][y - 1] = a[y - 1][x - 1] = 1

max_size = 0
for mask in range(1, 1 << n):
    if all(check(mask, a[i]) for i in range(n) if mask & (1 << i)):
        max_size = max(max_size, bin(mask)[2:].count("1"))

print(max_size)