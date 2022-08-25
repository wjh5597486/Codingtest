from collections import deque

def solution():
    N = int(input())
    G = [[0] * N for i in range(N)]
    for i in range(int(input())):
        r, c = map(int, input().split())
        r -= 1
        c -= 1
        G[r][c] = 1

    command = [list(input().split()) for i in range(int(input()))]
    command.append((10000, "D"))

    C = [[0] * N for i in range(N)]
    dq = deque()
    dq.append([0, 0])
    v_r = 0
    v_c = 1
    cur_r = 0
    cur_c = 0
    cnt = 0
    C[cur_r][cur_c] = 1
    for time, direct in command:
        time = int(time) - cnt
        for i in range(time):
            cnt += 1
            cur_r += v_r
            cur_c += v_c
            if 0 <= cur_r < N and 0 <= cur_c < N and C[cur_r][cur_c] == 0:
                if G[cur_r][cur_c] == 1:
                    G[cur_r][cur_c] = 0
                else:
                    r, c = dq.popleft()
                    C[r][c] = 0
                dq.append([cur_r, cur_c])
                C[cur_r][cur_c] = 1
            else:
                print(cnt)
                return

        if direct == "D":
            v_r, v_c = v_c, v_r
            if v_r == 0:
                v_c *= -1
        else:
            v_r, v_c = v_c, v_r
            if v_c == 0:
                v_r *= -1





if __name__ == '__main__':
    solution()
