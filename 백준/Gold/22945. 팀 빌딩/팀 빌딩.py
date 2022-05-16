import sys


def solution():
    L = 0
    R = int(input()) - 1
    G = list(map(int, sys.stdin.readline().split()))

    result = 0
    while L < R - 1:
        result = max(result, min(G[L], G[R]) * (R-L-1))

        if G[L] < G[R]:
            L += 1
        elif G[L] > G[R]:
            R -= 1
        else:
            if G[L+1] < G[R-1]:
                R -= 1
            else:
                L += 1
    print(result)
if __name__ == "__main__":
    solution()
