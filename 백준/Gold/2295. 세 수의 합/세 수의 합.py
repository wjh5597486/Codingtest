import sys
# sys.setrecursionlimit(10**6)
def solution():
    S = set()
    G = [int(sys.stdin.readline()) for _ in range(int(input()))]
    G = list(set(G))
    N = len(G)
    for i in range(N):
        for j in range(N):
            S.add(G[i]+G[j])

    G.sort(reverse=True)

    for i in range(N):
        for j in range(N):
            if G[i] - G[j] in S:
                print(G[i])
                return


if __name__ == "__main__":
    solution()
