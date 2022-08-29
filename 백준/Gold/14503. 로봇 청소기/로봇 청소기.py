from collections import deque
inf = float("inf")

def solution():
    R, C = map(int, input().split())
    x, y, d = map(int, input().split())
    G = [list(map(int, input().split())) for i in range(R)]
    d # 0북쪽 1 동쪽을, 2 남쪽을, 3 서쪽
    nxt_direction = [[[0, -1],[1, 0], [0, 1], [-1, 0]], # 서 남 동 북
                    [[-1, 0], [0, -1], [1, 0], [0, 1]], # 북 서 남 동
                    [[0, 1], [-1, 0], [0, -1], [1, 0]], # 동 북 서 남
                    [[1, 0], [0, 1], [-1, 0], [0, -1]], # 남 동 북 서
                     ]

    cnt = 0
    while True:
        if G[x][y] == 0:
            G[x][y] = -1
            cnt += 1

        switch = 0
        for idx, (xx, yy) in enumerate(nxt_direction[d]): # 왼쪽방향부터 차례대로 탐색을 진행한다.
            x2 = x + xx
            y2 = y + yy

            if G[x2][y2] == 0:  # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면,
                d += 3 - idx
                d %= 4  # 그 방향으로 회전한 다음
                x, y = x2, y2  # 다음 한 칸을 전진하고
                G[x2][y2] = -1  # 현재 위치를 청소한다.
                cnt += 1
                switch = 1
                break

        if switch == 1:
            continue

        x -= xx
        y -= yy
        if G[x][y] != 1:
            continue
        break

    print(cnt)


if __name__ == '__main__':
    solution()
