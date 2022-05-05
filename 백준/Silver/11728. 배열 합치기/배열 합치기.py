import sys


def solution():
    input()
    N = list(map(int, sys.stdin.readline().split()))
    G = list(map(int, sys.stdin.readline().split()))

    result = sorted([*N, *G])
    print(*result)





if __name__ == '__main__':
    solution()
