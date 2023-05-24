import sys

with open("salesman2.txt") as file:
    # Distances between cities
    graph = []
    n = file.readline().strip('\n')
    for line in file:
        l = line.strip('\n').split(" ")
        l = [int(s) for s in l]
        graph.append((l))

    n = len(graph)

# Implementation of the traveling salesman problem in Python using bit masks method to find the shortest route
def tsp(mask, cur, dist, dp, n, graph):
    if mask == ((1 << n) - 1):
        return dist[cur][0]

    if dp[mask][cur] != -1:
        return dp[mask][cur]

    ans = sys.maxsize
    for i in range(n):
        if mask & (1 << i) == 0:
            newMask = mask | (1 << i)
            newDist = dist[cur][i] + tsp(newMask, i, dist, dp, n, graph)
            ans = min(ans, newDist)

    dp[mask][cur] = ans
    return ans

def traveling_salesman(n, graph):
    dp = [[-1] * n for _ in range(1 << n)]
    return tsp(1, 0, graph, dp, n, graph)

print(traveling_salesman(n, graph))