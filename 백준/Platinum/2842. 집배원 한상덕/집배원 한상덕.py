import sys
from collections import deque


def solution():
    N = int(sys.stdin.readline())
    g = []
    for i in range(N):
        g.append(list(input()))

    goals = []
    for i in range(N):
        for j in range(N):
            if g[i][j] != '.':
                goals.append([i, j])

    G = []
    for i in range(N):
        G.append(list(map(int, sys.stdin.readline().split())))

    def bfs(left, right):
        visit = [[0] * N for _ in range(N)]
        Q = deque([(goals[0])])
        visit[goals[0][0]][goals[0][1]] = 1

        while Q:
            R, C = Q.popleft()
            for r, c in [[R + 1, C], [R + 1, C + 1], [R + 1, C - 1], [R, C + 1], [R, C - 1], [R - 1, C + 1],
                         [R - 1, C - 1], [R - 1, C]]:
                if 0 <= r < N and 0 <= c < N:
                    if visit[r][c] == 0 and left <= G[r][c] <= right:
                        visit[r][c] = 1
                        Q.append([r, c])

        for a, b in goals:
            if visit[a][b] == 0:
                return False
        return True

    p2 = set()
    for i in range(N):
        for j in range(N):
            p2.add(G[i][j])
    p2 = sorted(list(p2))

    init_i = float("inf")
    init_j = 0
    for x, y in goals:
        init_i = min(init_i, G[x][y])
        init_j = max(init_j, G[x][y])

    L = len(p2)
    i = 0
    j = p2.index(init_j)
    i_max = p2.index(init_i)
    result = float("inf")

    while j < L:
        l_num = p2[i]
        r_num = p2[j]
        if bfs(l_num, r_num):
            i += 1
            result = min(r_num - l_num, result)
            if i > i_max:
                break
        elif j < L - 1:
            j += 1
        else:
            break

    print(result)


if __name__ == '__main__':
    solution()
