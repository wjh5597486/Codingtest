import sys
def solution():
    N, K, D = map(int, sys.stdin.readline().split())
    graph = []
    for i in range(N):
        _, d = map(int, sys.stdin.readline().split())
        M = list(map(int, sys.stdin.readline().split()))
        graph.append([d, M])
    graph.sort()

    L = 0
    R = 1

    one_know = [0] * (K + 1)
    all_know = [0] * (K + 1)
    x0, y0 = graph[0]
    num_mem = 1
    for i in y0:
        one_know[i] += 1
        all_know[i] += 1

    result = 0

    while R < N:
        x0, y0 = graph[L]
        x1, y1 = graph[R]

        if x1 - x0 <= D:
            num_mem += 1
            for i in y1:
                one_know[i] += 1
                all_know[i] += 1
            R += 1
        else:
            num_mem -= 1
            for i in y0:
                one_know[i] -= 1
                all_know[i] -= 1
            L += 1
        A = K - one_know.count(0) + 1
        B = all_know.count(num_mem)
        result = max(result, (A-B)*num_mem)

    print(result)





if __name__ == "__main__":
    solution()
