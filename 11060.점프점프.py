from collections import deque

N = int(input())

graph = list(map(int, input().split()))

dq = deque()

dq.append([0,0])
result = -1

cost = [0] * N
while dq:
    x, y = dq.popleft()

    if x == N-1:
        result = y
        break

    for i in range(1, graph[x]+1):
        xi = x + i

        if xi >= N:
            continue

        if cost[xi] != 0:
            continue

        dq.append([xi, y+1])
        cost[xi] = y+1


print(result)