import sys
input = sys.stdin.readline

N, M = map(int, input().split())
inf = float("inf")

def go(G):
    cost = [[inf] * M for _ in range(N)]
    dq = []
    dq.append([0, 0, 1, 0])
    while dq:
        n, m, c, d = dq.pop() # c: chance
        for ni, mi in [[n + 1, m], [n, m + 1], [n - 1, m], [n, m - 1]]:
            if not (0 <= ni < N and 0 <= mi < M):  # range
                continue
            if cost[ni][mi] < d+1:  # low_cost
                continue
            if G[ni][mi] == 1:  # chance
                if c == 0:
                    continue
                else:
                    cost[ni][mi] = d + 1
                    dq.append([ni, mi, 0, d+1])
            else:
                cost[ni][mi] = d + 1
                dq.append([ni, mi, c, d+1])

    print(cost[-1][-1])

go(graph)



