import sys
from collections import deque

def solution():
    N = int(input())

    graph = [[] for i in range(N + 1)]

    for _ in range(N-1):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))  # child, cost
        graph[b].append((a, c))  # child, cost

    def que(idx):
        check = [0] * (N + 1)
        visit = [0] * (N + 1)
        visit[idx] = 1

        q = deque()
        q.append((idx, 0))

        while q:
            par, cost_sum = q.popleft()
            check[par] = cost_sum

            for child, cost in graph[par]:
                if visit[child] == 1:
                    continue
                visit[child] = 1
                q.append((child, cost + cost_sum))

        return max(check)

    result = 0
    for start in range(1, N + 1):
        result = max(que(start), result)
    print(result)

if __name__ == '__main__':
    solution()
