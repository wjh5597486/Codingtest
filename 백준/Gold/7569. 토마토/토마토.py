import sys
from collections import deque


def solution():
    C, R, D = map(int, sys.stdin.readline().split())
    G = []

    for i in range(D):
        A = [list(map(int, sys.stdin.readline().split())) for j in range(R)]
        G.append(A)
    A = []

    graph = [[[-1] * C for i in range(R)] for i in range(D)]

    dq = deque()
    for d in range(D):
        for r in range(R):
            for c in range(C):
                if G[d][r][c] == 1:
                    dq.append([d,r,c])
                    graph[d][r][c] = 0
                elif G[d][r][c] == 0:
                    A.append([d,r,c])

    while dq:
        d, r, c = dq.popleft()

        for d2, r2, c2 in [[d+1,r,c],[d-1,r,c],[d,r+1,c],[d,r-1,c],[d,r,c+1],[d,r,c-1]]:
            if 0<=d2<D and 0<=r2<R and 0<=c2<C and graph[d2][r2][c2] == -1 \
                    and G[d2][r2][c2] == 0:
                graph[d2][r2][c2] = graph[d][r][c] + 1
                dq.append([d2,r2,c2])
    none = 0
    day = 0
    for d, r, c in A:
        a = graph[d][r][c]
        day = max(a, day)
        if a == -1:
            none = True
            break

    if none:
        print(-1)
    else:
        print(day)








if __name__ == "__main__":
    solution()
