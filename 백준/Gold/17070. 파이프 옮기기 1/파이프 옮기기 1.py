import sys
def solution():
    N = int(input())
    G = []
    for i in range(N):
        G.append(list(map(int, sys.stdin.readline().split())))

    graph = [[[0,0,0] for i in range(N+1)]  for i in range(N+1)]
    graph[1][2] = [1,0,0] # right/ diagonal/ down

    for r in range(1, N+1):
        for c in range(1, N+1):
            if G[r-1][c-1]:
                continue
            else:
                Q = graph[r][c-1][0]+graph[r][c-1][1]  # from right
                if G[r-2][c-1] == 0 and G[r-1][c-2] == 0:
                    W = sum(graph[r-1][c-1][0:3])  # from diagonal
                else:
                    W = 0
                E = graph[r-1][c][2]+graph[r-1][c][1]  # from down
                graph[r][c][0] += Q
                graph[r][c][1] += W
                graph[r][c][2] += E

    print(sum(graph[-1][-1]))


if __name__ == "__main__":
    solution()


