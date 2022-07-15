from collections import deque


def solution():
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]

    dq = deque()

    for r in range(N):
        for c in range(N):
            if G[r][c] == 9:
                G[r][c] = 0
                dq.append((r, c, 0))

    step_count = 0
    shark_size = (2, 0)

    while True:
        check = [[0] * N for i in range(N)]
        fish_list = []
        while dq:
            r, c, n = dq.popleft()
            if fish_list != [] and fish_list[0][2] <= n:
                continue
            for r2, c2 in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if 0 <= r2 < N and 0 <= c2 < N:
                    if check[r2][c2] == 1:
                        continue
                    check[r2][c2] = 1
                    if G[r2][c2] > shark_size[0]:
                        continue
                    if 0 < G[r2][c2] < shark_size[0]:  # eat
                        fish_list.append([r2, c2, n+1])
                    dq.append((r2, c2, n+1))

        fish_list.sort(key=lambda x:[x[2],x[0],x[1]])


        if fish_list == []:
            break

        r, c, step = fish_list[0]
        G[r][c] = 0
        step_count += step
        dq.append([r, c, 0])

        if shark_size[0] == shark_size[1] + 1:
            shark_size = (shark_size[0]+1, 0)
        else:
            shark_size = (shark_size[0], shark_size[1] + 1)

    print(step_count)


if __name__ == '__main__':
    solution()
