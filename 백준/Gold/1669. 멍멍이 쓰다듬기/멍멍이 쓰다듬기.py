def solution():
    N, K = map(int, input().split())
    cur_speed = 0
    for i in range(0, 1_000_000):
        if N == K:
            print(i)
            break
        rest = K - N
        for j in [1, 0, -1]:
            nxt_speed = cur_speed + j
            break_dst = int((nxt_speed + 1) * nxt_speed / 2)

            if break_dst <= rest:
                cur_speed = nxt_speed
                break
        N += cur_speed


if __name__ == '__main__':
    solution()
