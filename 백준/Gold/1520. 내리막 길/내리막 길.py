import sys
sys.setrecursionlimit(10**6)
def solution():
    R, C = map(int, sys.stdin.readline().split())
    G = [list(map(int, sys.stdin.readline().split())) for i in range(R)]

    graph = [[-1]*C for i in range(R)]
    graph[0][0] = 1

    def call(r, c):
        if graph[r][c] != -1:
            return graph[r][c]
        else:
            result = 0
            for r2, c2 in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if r2 == -1 or r2 == R or c2 == -1 or c2 == C:
                    continue
                if G[r][c] < G[r2][c2]:
                    result += call(r2, c2)

            graph[r][c] = result
            return result


    X = call(R-1, C-1)
    print(X)


if __name__ == "__main__":
    solution()
