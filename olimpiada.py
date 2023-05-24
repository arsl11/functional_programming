def solve(t, n, a):
    tasks = [(t // a[i], a[i]) for i in range(n)]
    tasks.sort(reverse=True)
    penalty = 0
    solved = 0
    times = []
    for i in range(n):
        sth, time = tasks[i]
        if t >= time:
            if i == 0:
                times.append(time)
            else:
                l = len(times)
                times.append(times[l - 1] + time)
            t -= time
            solved += 1
        else:
            break
    
    for time in times:
        penalty += time

    return solved, penalty


n = 1000 
t = 50000
items = []
with open('contest.txt', 'r') as file:
    for line in file:
        items = line.split(" ")

for i in range(len(items)):
    items[i] = int(items[i])

print(solve(t, n, items))
