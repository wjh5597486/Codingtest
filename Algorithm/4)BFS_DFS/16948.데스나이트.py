from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

graph = [[0]*N for _ in range(N)]

dq = deque()
dq.append([r1,c1,0])
result = -1

while dq:
    r, c, cost = dq.popleft()
    if r==r2 and c==c2:
        result = cost
        break
    for ri, ci in [[r-2,c-1],[r-2,c+1],[r,c-2],[r,c+2],[r+2,c-1],[r+2,c+1]]:
        if 0<=ri<N and 0<=ci<N:
            if graph[ri][ci]==0:
                graph[ri][ci] = 1
                dq.append([ri,ci,cost+1])

print(result)