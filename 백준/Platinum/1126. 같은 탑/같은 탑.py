import sys
inf = float("inf")

def solution():
    N = int(input())
    graph = list(map(int, input().split()))
    num = sum(graph)
    max_num = 2*num+1

    G = [[-inf] * (max_num+1) for i in range(N+1)]

    for i in range(N+1):
        G[i][num] = 0

    for n, height in enumerate(graph):
        for i in range(max_num+1):

            i_m = i - height
            i_p = i + height

            if 0 <= i_m and i_p < max_num:
                G[n][i] = max(G[n-1][i_m] + height, G[n-1][i], G[n-1][i_p])

            elif i_p >= max_num:
                G[n][i] = max(G[n-1][i_m] + height, G[n-1][i])

            elif 0 > i_m:
                G[n][i] = max(G[n-1][i], G[n-1][i + height])

    if G[-2][num] == 0:
        print(-1)
    else:
        print(G[-2][num])


if __name__ == '__main__':
    solution()
