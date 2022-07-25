from collections import deque
def solution():

    N = int(input())
    M = int(input())

    G = [[] for i in range(N+1)]
    for i in range(M):
        a, b, c = map(int, input().split())
        G[a].append([c, b])  # cost, idx

    for start in range(1,N+1):
        inf = float("inf")
        check = [inf for i in range(N+1)]
        check[start] = 0
        q = deque()
        q.append((0, start))  # cost, cur

        while q:
            cost_sum, cur = q.popleft()
            for cost, nxt in G[cur]:
                if cost_sum + cost < check[nxt]:
                    check[nxt] = cost_sum + cost
                    q.append((check[nxt], nxt))
        print(*[i if i!=inf else 0 for i in check[1::]])


if __name__ == '__main__':
    solution()
