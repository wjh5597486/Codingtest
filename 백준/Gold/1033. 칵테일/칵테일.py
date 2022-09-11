import math
def solution():
    N = int(input())
    graph = [[False] * N for i in range(N)]
    for i in range(N-1):
        a, b, p, q = map(int, input().split())
        graph[a][b] = (q, p)
        graph[b][a] = (p, q)

    G = [-1] * N
    G[0] = 1
    cnt = 1
    dq = [0]
    while dq:
        cur = dq.pop()
        for nxt in range(N):
            if graph[cur][nxt] and G[nxt] < 0:
                p, q = graph[cur][nxt]
                G[nxt] = G[cur] * p/q
                dq.append(nxt)
                cnt *= q

    for i in range(N):
        G[i] = round(G[i]*cnt)
    n = math.gcd(*G)

    for i in range(N):
        G[i] //= n
    print(*G)


if __name__ == "__main__":
    solution()