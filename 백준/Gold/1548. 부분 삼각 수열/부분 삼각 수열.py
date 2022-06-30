def solution():
    N = int(input())
    G = list(map(int, input().split()))
    G.sort()
    result = 1
    if len(G) <= 2:
        print(len(G))
        return

    for a in range(0, N-1):
        if G[a]*2 > G[a+1]:
            result = 2

    for a in range(0, N-2):
        temp = 0
        for c in range(a+2, N):
            if G[a] + G[a+1] > G[c]:
                if temp == 0:
                    temp = 3
                else:
                    temp += 1

                result = max(result, temp)
            else:
                break

    print(result)


if __name__ == '__main__':
    solution()