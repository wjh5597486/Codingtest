import sys

def solution():
    N = int(input())
    G = list(map(int, sys.stdin.readline().split()))
    G.sort()
    L = 0
    R = N-1
    result = float("inf")

    while L < R:
        sum0 = G[L] + G[R]
        if abs(result) > abs(sum0):
            result = sum0
        sum1 = abs(G[L+1] + G[R])
        sum2 = abs(G[L] + G[R-1])
        if sum1 < sum2:
            L += 1
        else:
            R -= 1

    print(result)



if __name__ == '__main__':
    solution()
