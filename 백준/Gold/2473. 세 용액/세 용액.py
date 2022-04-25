# import sys
# N = int(sys.stdin.readline())
# M = sys.stdin.readline()

#https://www.acmicpc.net/problem/2473

def solution():
    N = int(input())
    G = list(map(int, input().split()))
    G.sort()
    result = float("inf")
    for i in range(N-2):
        L = i+1
        R = N-1

        while L < R:
            sum0 = G[i] + G[L] + G[R]
            if abs(sum0) <= abs(result):
                r_list = [G[i], G[L], G[R]]
                result = sum0
            if sum0 < 0:
                L += 1
            elif sum0 > 0:
                R -= 1
            else:
                print(*r_list)
                return 0
    print(*r_list)

if __name__ == '__main__':
    solution()