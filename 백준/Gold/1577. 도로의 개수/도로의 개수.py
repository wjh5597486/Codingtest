from collections import deque
def solution():
    R, C = map(int, input().split())
    road = set()
    R += 1
    C += 1

    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        road.add((a, b, c, d))
        road.add((c, d, a, b))

    inf = float("inf")
    graph = [[0] * C for i in range(R)]
    visit = [[0] * C for i in range(R)]
    dq = deque()
    dq.append([0, 0])
    graph[0][0] = 1

    while dq:
        r, c = dq.popleft()
        for r2, c2 in [[r + 1, c], [r, c + 1]]:
            if (r, c, r2, c2) in road:
                continue

            if 0 <= r2 < R and 0 <= c2 < C:
                graph[r2][c2] += graph[r][c]

                if visit[r2][c2] == 0:
                    visit[r2][c2] = 1
                    dq.append([r2, c2])

    print(graph[-1][-1])
if __name__ == '__main__':
    solution()
