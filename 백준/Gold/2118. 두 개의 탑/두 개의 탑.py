import sys
def solution():
    N = int(sys.stdin.readline())
    G = [0] * N * 2
    for i in range(N):
        n = int(sys.stdin.readline())
        G[i], G[i+N] = n, n
    left_sum = sum(G[0:N-1])
    right_sum = G[N-1]
    left = 0
    right = N-1
    result = 0
    while left < right:
        if left_sum > right_sum:
            left_sum -= G[left]
            right_sum += G[left]
            left += 1

        elif left_sum <= right_sum:
            right_sum -= G[right]
            left_sum += G[right]
            right += 1

        if right == N*2:
            break
        result = max(result, min(left_sum, right_sum))


    print(result)

if __name__ == "__main__":
    solution()
