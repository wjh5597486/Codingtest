from collections import deque
def solution():
    N, M = map(int, input().split())
    G = [list() for i in range(N+1)]
    for i in range(N-1):
        n, m, k = map(int, input().split())
        G[n].append([m, k])
        G[m].append([n, k])

    for _ in range(M):
        start, end = map(int, input().split())
        visit = [-1] *(N+1)
        visit[start] = 0
        q = deque()
        q.append(start)
        while q:
            cur = q.popleft()
            if cur == end:
                break
            for next_node, distance in G[cur]:
                if visit[next_node] > -1:
                    continue
                visit[next_node] = visit[cur] + distance
                q.append(next_node)
        print(visit[end])

if __name__ == "__main__":
    solution()