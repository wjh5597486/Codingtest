from collections import deque

def DPS(mmm, n, m):
    dq = deque()
    mmm[0][0] = 1
    dq.append([0, 0])
    while dq:
        h, w = dq.popleft()

        for hi, wi in [[h-1, w],[h+1, w],[h, w-1],[h, w+1]]:
            if 0 <= hi < n and 0 <= wi < m:
                if mmm[h][w] + 1 < mmm[hi][wi]:
                    dq.append([hi, wi])
                    mmm[hi][wi] = mmm[h][w] + 1

    return mmm[-1][-1]


# mmm = [
#     [0,1,0,0],
#     [1,1,1,0],
#     [1,0,0,0],
#     [0,0,0,0],
#     [0,1,1,1],
#     [0,0,0,0]
# ]
# n, m = 1,1
n, m = map(int, input().split())
mmm = []
for i in range(n):
    mmm.append(list(map(int, input().split())))
# wall detector
inf = float("inf")
walls = []
for i in range(n):
    for j in range(m):
        if mmm[i][j] == 1:
            walls.append([i, j])
        if mmm[i][j] == 0:
            mmm[i][j] = inf
        else:
            mmm[i][j] = 0



result = inf

for i, j in walls:
    map2 = [item[:] for item in mmm]
    map2[i][j] = inf
    result = min(result, DPS(map2, n, m))
if result == inf:
    result = -1

if n ==1 and m==1:
    print(1)
else: print(result)


