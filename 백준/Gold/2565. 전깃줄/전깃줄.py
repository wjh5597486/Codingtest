import sys
def solution():
    N = int(input())
    G = []
    for i in range(N):
        G.append(list(map(int, sys.stdin.readline().split())))
    G.sort()
    acc = [1] * N

    for i in range(1, N):
        for j in range(i):
            if G[i][1] > G[j][1]:
                acc[i] = max(acc[i], acc[j] + 1)
    print(N- max(acc))

if __name__ == "__main__":
    solution()


