import sys
def solution():
    N = int(sys.stdin.readline())
    G = list(map(int, sys.stdin.readline().split()))
    G.sort()
    result = float("inf")

    for i in range(N-3):
        for j in range(i+3, N):
            L = i+1
            R = j-1
            sum0 = G[i] + G[j]

            while L < R:
                sum1 = G[L] + G[R]
                sumsum = abs(sum0 - sum1)
                result = min(sumsum, result)

                if sum0 > sum1:
                    L += 1
                elif sum0 < sum1:
                    R -= 1
                else:
                    print(0)
                    return 0

    print(result)



if __name__ == '__main__':
    solution()
