import sys
def solution():
    N = int(input())
    G = list(map(int, sys.stdin.readline().split()))
    N = len(G)
    graph = [[0] * N for i in range(N)]
    for i in range(N):
        graph[i][i] = 1

    for right, num in enumerate(G):
        for left in range(right):
            if G[left] == num and (left+1 == right or graph[left+1][right-1] == 1):
                graph[left][right] = 1
                graph[right][left] = 1

    # for i in graph:
    #     print(i)

    for i in range(int(input())):
        a, b = map(int, sys.stdin.readline().split())
        print(graph[a-1][b-1])



if __name__ == '__main__':
    solution()
