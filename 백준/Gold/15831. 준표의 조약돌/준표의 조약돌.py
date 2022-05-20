import sys
def solution():
    N, max_b, min_w = map(int, sys.stdin.readline().split())
    G = list(i for i in sys.stdin.readline())
    graph = [0, 0] # W, B
    L, R = 0, 0
    W, B = "W", "B"

    if G[0] == W:
        graph[0] += 1
    else:
        graph[1] += 1
    result = 0

    while True:
        if graph[1] <= max_b: # 흑 ok, R+=1
            if graph[0] >= min_w:
                result = max(result, sum(graph))
            R += 1
            if R == N:
                break
            if G[R] == W:
                graph[0] += 1
            else:
                graph[1] += 1

        else:  # 흑 많아 L+=1
            if G[L] == W:
                graph[0] -= 1
            else:
                graph[1] -= 1
            L += 1
            if L == N:
                break

    print(result)


if __name__ == "__main__":
    solution()
