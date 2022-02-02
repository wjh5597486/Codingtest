from collections import deque

ladder = list(range(150))
N, M = map(int, input().split())
for i in range(N+M):
    x, y = map(int, input().split())
    ladder[x] = y
dq = deque()


dq.append([0, 1]) # 0th dice, 0th location
inf = float("inf") # inf
check = [inf] * 150

while check[100] == inf:
    dice, loca = dq.popleft()

    for i in range(1, 7):
        if check[loca + i] == inf:
            moveLoca = ladder[loca + i]
            check[ladder[loca + i]] = dice + 1
            dq.append([dice + 1, moveLoca])

print(check[100])