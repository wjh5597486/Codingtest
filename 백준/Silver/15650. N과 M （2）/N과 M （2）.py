def solution():
    N, M = map(int, input().split())
    G = [[] for _ in range(10)]
    G[1] = [[i] for i in range(1, N+1)]

    for i in range(1, M):
        for line in G[i]:
            for k in range(line[-1]+1, N+1):
                G[i+1].append(line + [k])

    G[M].sort(key=lambda x:[x[i] for i in range(M)])

    for i in G[M]:
        print(*i)

if __name__ == '__main__':
    solution()
