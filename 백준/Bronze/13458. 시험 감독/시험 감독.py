from collections import deque
inf = float("inf")

def solution():
    K = int(input())
    G = list(map(int, input().split()))
    N, M = map(int, input().split())

    cnt = K

    for i in range(K):
        G[i] = max(0, G[i]-N)
        cnt += G[i] // M
        if G[i] % M > 0:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    solution()
