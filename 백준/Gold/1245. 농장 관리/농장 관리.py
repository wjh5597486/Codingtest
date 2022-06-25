import sys


def solution():
    R, C = map(int, input().split())
    G = []
    for i in range(R):
        G.append(list(map(int, sys.stdin.readline().split())))

    def checker(r, c):
        num = G[r][c]
        q = [[r, c]]
        visit[r][c] = 1
        top = 1
        while q:
            row, col = q.pop()
            for row2, col2 in [[row + 1, col + 1], [row + 1, col - 1], [row + 1, col], [row - 1, col], [row - 1, col - 1], [row - 1, col + 1], [row, col + 1], [row, col - 1]]:
                if 0 <= row2 < R and 0 <= col2 < C:
                    if G[row2][col2] > num:
                        top = 0
                    if visit[row2][col2] == 1:
                        continue
                    if G[row2][col2] == num:
                        q.append([row2, col2])
                        visit[row2][col2] = 1
        return top

    H = max(map(max, G))
    result = 0
    for N in range(1, H + 1):
        visit = [[0] * C for i in range(R)]
        for c in range(C):
            for r in range(R):
                if visit[r][c] == 0 and G[r][c] == N:
                    result += checker(r, c)

    print(result)


if __name__ == "__main__":
    solution()
