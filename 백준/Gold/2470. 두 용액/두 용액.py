def solution():
    N = int(input())
    G = list(map(int, input().split()))
    G.sort()
    l, r = 0, N-1
    minimum = float("inf")
    result = [G[l],G[r]]
    while l < r:
        if abs(minimum) > abs(G[l] + G[r]):
            minimum = G[l] + G[r]
            result = [G[l], G[r]]

        sum1 = abs(G[l+1] + G[r])
        sum2 = abs(G[l] + G[r-1])
        if sum1 < sum2:
            l += 1
        else:
            r -= 1
    print(*result)

if __name__ == '__main__':
    solution()