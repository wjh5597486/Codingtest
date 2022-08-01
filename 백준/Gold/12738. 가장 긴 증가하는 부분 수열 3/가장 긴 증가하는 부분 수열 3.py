import sys
inf = float("inf")
def solution():
    input()
    G = list(map(int, sys.stdin.readline().split()))

    def find(num):
        if graph[-1] < num:
            graph.append(num)
            return len(graph)-1

        l, r = 0, len(graph)-1

        while l < r:
            mid = (l + r) // 2
            if graph[mid] < num:
                l = mid + 1

            else:
                r = mid
        return l

    graph = [-inf]

    for num in G:
        idx = find(num)
        graph[idx] = num

    print(len(graph)-1)




if __name__ == '__main__':
    solution()
