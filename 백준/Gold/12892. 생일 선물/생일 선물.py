import sys
def solution():
    N, D = map(int, sys.stdin.readline().split())
    G = []
    for i in range(N):
        G.append(list(map(int, sys.stdin.readline().split())))
    G.sort()
    L = 0
    R = 0
    p1, v1 = G[0]
    result = 0
    MAX = 0

    while R < N:
        p2, v2 = G[R]

        if p2 - p1 >= D:
            result -= v1
            L += 1
            p1, v1 = G[L]
        else:
            result += v2
            MAX = max(result, MAX)
            R += 1

    print(MAX)

if __name__ == "__main__":
    solution()
