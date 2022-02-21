from collections import deque

N, M = map(int, input().split())
Nq = deque()

Nq.append([0, N])  # time, coordinate.

leng = 500001
INF = float("inf")
graph = [[INF, INF] for __ in range(leng)]
graph[N][0] = 0

while Nq:  # 언니
    time, X = Nq.popleft()
    flag = 1 - time % 2
    for xi in [X + 1, X - 1, X * 2]:
        if 0 <= xi < leng and graph[xi][flag] > time + 1:  # even
            graph[xi][flag] = time + 1
            Nq.append([time + 1, xi])

t = 0
flag = 0
result = -1
while M < leng:
    if graph[M][flag] != INF and graph[M][flag] <= t:
        result = t
        break
    flag = 1 - flag
    t += 1
    M += t

print(result)


