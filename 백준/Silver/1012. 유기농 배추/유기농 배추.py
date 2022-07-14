from collections import deque


def solution():
    cases = int(input())
    for i in range(cases):  # cases
        R, C, num = map(int, input().split())
        G = [[0] * C for _ in range(R)]
        visit = [[0] * C for _ in range(R)]

        for i in range(num):
            r, c = map(int, input().split())
            G[r][c] = 1

        dq = deque()
        cnt = 0
        for r in range(R):
            for c in range(C):
                if G[r][c] == 1 and visit[r][c] == 0:
                    cnt += 1
                    dq.append((r, c))
                    visit[r][c] = 1

                    while dq:
                        r1, c1 = dq.pop()

                        for r2, c2 in [[r1 + 1, c1], [r1 - 1, c1], [r1, c1 + 1], [r1, c1 - 1]]:
                            if 0 <= r2 < R and 0 <= c2 < C:
                                if visit[r2][c2] == 0 and G[r2][c2] == 1:
                                    dq.append((r2, c2))
                                    visit[r2][c2] = 1
        print(cnt)


if __name__ == '__main__':
    solution()
