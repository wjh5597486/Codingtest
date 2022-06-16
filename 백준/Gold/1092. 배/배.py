import sys
# sys.setrecursionlimit(10**6)

def solution():
    N = int(input())
    G = list(map(int, input().split()))
    G.sort()
    K = int(input())
    graph = list(map(int, sys.stdin.readline().split()))
    Q = [0] * N
    for i in graph:
        switch = 1
        for j in range(N):
            if i <= G[j]:
                Q[j] += 1
                switch = 0
                break
        if switch:
            print(-1)
            return

    Q.reverse()
    time = 0
    crane = 0
    rest = 0

    for i in range(0, N):
        crane += 1
        Q[i] -= rest + time
        rest = 0
        while Q[i] > 0:
            time += 1
            Q[i] -= crane
        if Q[i] < 0:
            rest = -Q[i]
    print(time)



if __name__ == "__main__":
    solution()
