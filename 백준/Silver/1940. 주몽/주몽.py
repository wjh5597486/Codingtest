import sys


def solution():
    L = 0
    R = int(input()) - 1
    M = int(input())
    G = list(map(int, sys.stdin.readline().split()))
    G.sort()
    result = 0
    while L < R:
        S = G[L] + G[R]
        if S == M:
            result += 1
            R -= 1
            L += 1

        elif S > M:
            R -= 1

        else:
            L += 1
    print(result)


if __name__ == "__main__":
    solution()
