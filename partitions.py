def partitions(n, k=1):
    if n == 0:
        return [[]]
    result = []
    for i in range(k, n + 1):
        for p in partitions(n - i, i):
            result.append([i] + p)
    return result
 
 
result = partitions(35)
print(result[13671])
