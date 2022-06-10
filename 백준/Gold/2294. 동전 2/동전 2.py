import sys
sys.setrecursionlimit(10**6)

def solution():
    G = [11000] * 10001
    G[0] = 0

    N, K = map(int, input().split())
    sets = set()

    for i in range(N):
        sets.add(int(input()))
    S = sorted(list(sets))

    for n in S:
        for i in range(n, 10001):
            G[i] = min(G[i-n]+1, G[i])

    if G[K] >= 10001:
        print(-1)
    else:
        print(G[K])





if __name__ == "__main__":
    solution()
