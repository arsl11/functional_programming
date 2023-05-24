from itertools import islice

wt = []
val = []
# чтение предметов из файла
with open('rucksack.txt', 'r') as file:
    n, W = file.readline().strip('\n').split(" ")
    n = int(n)
    W = int(W)
    for line in file:
        weight, value = map(int, line.split())
        wt.append(weight)
        val.append(value)


def rucksack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
 
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    
    res = []
    i, w = n, W
    while i > 0 and w > 0:
        if K[i][w] != K[i - 1][w]:
            res.append(i)
            w -= wt[i - 1]
        i -= 1
    res.reverse()
 
    return K[n][W], res


print(rucksack(W, wt, val, n))

