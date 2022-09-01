def solution():
    N = int(input())
    G = list(map(int, input().split()))
    dp = [1] * (N+1)
    for i in range(len(G)):
        for j in range(i):
            if G[j] < G[i]:
                dp[i] = max(dp[i], dp[j] + 1)


    G = G[::-1]
    dp2 = [1] * (N+1)

    for i in range(1, len(G)):
        for j in range(i):
            if G[j] < G[i]:
                dp2[i] = max(dp2[i], dp2[j] + 1)
    dp2 = dp2[::-1]

    result = max([dp[i] + dp2[i+1] for i in range((N))]) - 1

    print(result)



if __name__ == "__main__":
    solution()
