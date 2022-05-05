import sys


def solution():
    N, M = map(int, input().split())
    G = list(map(int, sys.stdin.readline().split()))
    sum0 = sum(G[:M])
    L = 0
    R = M
    result = sum0
    while R < N:
        sum0 += G[R] - G[L]
        result = max(sum0, result)
        L += 1
        R += 1
    print(result)


if __name__ == '__main__':
    solution()
