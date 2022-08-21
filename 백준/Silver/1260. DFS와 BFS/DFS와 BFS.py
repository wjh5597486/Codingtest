import sys
from collections import deque
def solution():
    N, M, V = map(int, input().split())
    G = [[] for i in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    for i in G:
        i.sort()
        
    def bfs(a):
        visit = [0] * (N+1)
        visit[a] = 1
        dq = deque([a])
        result = []
        while dq:
            cur = dq.popleft()
            result.append(cur)
            for nxt in G[cur]:
                if visit[nxt] == 0:
                    visit[nxt] = 1
                    dq.append(nxt)
        print(*result)

    def dfs(a):
        dq = deque([a])
        while dq:
            cur = dq.popleft()
            result.append(cur)
            for nxt in G[cur]:
                if visit[nxt] == 0:
                    visit[nxt] = 1
                    dfs(nxt)

    visit = [0] * (N + 1)
    visit[V] = 1
    result = []
    dfs(V)
    print(*result)
    bfs(V)

if __name__ == '__main__':
    solution()
