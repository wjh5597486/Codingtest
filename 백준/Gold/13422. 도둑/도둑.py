# https://www.acmicpc.net/problem/1484
def solution():
    for i in range(int(input())):
        N, M, K = map(int, input().split())
        G = list(map(int, input().split()))
        if N != M:
            G = G + G[:M-1]

        l = 0
        r = l + M - 1

        result = 0
        cur_sum = sum(G[l:r + 1])

        while True:
            if cur_sum < K:
                result += 1
            l += 1
            r += 1
            if r < len(G):
                cur_sum = - G[l - 1] + cur_sum + G[r]
            else:
                break

        print(result)


if __name__ == '__main__':
    solution()
