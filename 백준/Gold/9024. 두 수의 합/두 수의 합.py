import sys


def solution():
    for i in range(int(input())):
        N, K = map(int, sys.stdin.readline().split())
        G = list(map(int, sys.stdin.readline().split()))
        G.sort()

        min_value = float("inf")

        l = 0
        r = N - 1

        while l < r:
            sum0 = G[l] + G[r]

            if abs(K - sum0) < min_value:
                result = 1
                min_value = abs(K - sum0)

            elif abs(K - sum0) == min_value:
                result += 1

            if sum0 > K:
                r -= 1
            else:
                l += 1

        print(result)


if __name__ == "__main__":
    solution()
