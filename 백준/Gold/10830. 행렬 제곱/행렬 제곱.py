from collections import deque
inf = float("inf")
import sys
sys.setrecursionlimit(10**4)

def solution():
    def multi(P, Q):
        graph = [[0] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                row = P[r]
                col = [Q[i][c] for i in range(N)]
                graph[r][c] = sum([row[i] * col[i] for i in range(N)]) % 1000

        return graph

    def rec(P, B):
        if B == 2:
            return multi(P, P)

        if B == 1:
            return P

        if B % 2 == 0:
            return rec(rec(P, B//2), 2)

        else:
            return multi(rec(rec(P, B//2), 2), G)


    N, B = map(int, input().split())
    G = [list(map(int, input().split())) for _ in range(N)]


    result = rec(G, B)
    for r in range(N):
        for c in range(N):
            result[r][c] %= 1000
    for i in result:
        print(*i)





if __name__ == '__main__':
    solution()
