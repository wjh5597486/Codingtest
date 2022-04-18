def solution():
    N, M = map(int, input().split())
    G = [int(input()) for _ in range(N)]
    G.sort()
    l = 0
    r = 0
    result = float("inf")
    while r < N and l < N:
        gap = abs(G[l] - G[r])
        if gap < M:
            r +=1
        else:
            if gap >= M and gap < result:
                result = gap
            l +=1

    print(result)


if __name__ == '__main__':
    solution()
