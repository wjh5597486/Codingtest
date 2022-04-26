# import sys
# N = int(sys.stdin.readline())
# M = sys.stdin.readline()

#https://www.acmicpc.net/problem/2473

def solution():
    N = int(input())
    if N == 1:
        print(0)
        return 0
    G = list(range(2, N+100))
    for i in range(len(G)):
        F = G[i]
        if F == 0:
            continue

        X = 2
        while F*X <= N:
            G[F*X-2] = 0
            X += 1

    G = [x for x in G if x != 0]

    result = 0
    if N in G:
        result += 1

    l = 0
    r = 1
    S = G[0]+G[1]
    while l < r:
        if S < N:
            r += 1
            S += G[r]
        elif N < S:
            S -= G[l]
            l += 1
        else:
            result += 1
            r += 1
            S += G[r]
    print(result)



if __name__ == '__main__':
    solution()