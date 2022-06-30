import sys
from collections import deque

def solution():
    K = 501
    graph = [[0] * K for _ in range(K)]
    for j in range(1, 3):
        for i in range(int(input())):
            x1, y1, x2, y2 = map(int, input().split())

            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    graph[x][y] = j

    dq = deque()
    dq.append([0, 0])
    inf = float("inf")
    visit = [[inf] * K for _ in range(K)]
    visit[0][0] = 0

    while dq:
        r, c = dq.popleft()
        for r2, c2 in [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]:
            if 0 <= r2 < K and 0 <= c2 < K:
                if graph[r2][c2] == 2:
                    continue

                danger = 1 if graph[r2][c2] == 1 else 0

                if visit[r2][c2] > visit[r][c] + danger:
                    visit[r2][c2] = danger + visit[r][c]
                    dq.append([r2, c2])

    if visit[-1][-1] == inf:
        print(-1)
    else:
        print(visit[-1][-1])

if __name__ == "__main__":
    solution()