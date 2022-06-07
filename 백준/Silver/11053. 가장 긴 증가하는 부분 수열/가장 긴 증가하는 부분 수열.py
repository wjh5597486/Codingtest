def solution():
    N = int(input())
    G = list(map(int, input().split()))
    dp = [1] * 1001

    for i in range(len(G)):
        for j in range(i):
            if G[j] < G[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))


if __name__ == "__main__":
    solution()
