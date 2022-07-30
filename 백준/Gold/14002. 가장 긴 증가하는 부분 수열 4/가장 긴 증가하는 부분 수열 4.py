import sys
def solution():
    N = int(input())
    G = list(map(int, sys.stdin.readline().split()))

    def find(num):
        if graph[-1] < num:
            graph.append(num)
            P.append([])
            return len(graph) - 1

        l = 0
        r = len(graph) - 1
        while l < r:
            mid = (l + r) // 2
            if graph[mid] < num:
                l = mid + 1
            else:
                r = mid
        return l

    graph = [-1]
    P = [[]]

    for idx, num in enumerate(G):
        position = find(num)
        graph[position] = num
        P[position].append((idx, num))

    X = len(P) - 1
    result = []
    idx = float("inf")
    number = float("inf")

    for i in range(X, 0, -1):
        for nxt_idx, nxt_num in P[i]:
            if nxt_idx < idx and nxt_num < number:
                number = nxt_num
                idx = nxt_idx
                result.append(number)
                break

    print(len(result))
    print(*result[::-1])


if __name__ == '__main__':
    solution()
