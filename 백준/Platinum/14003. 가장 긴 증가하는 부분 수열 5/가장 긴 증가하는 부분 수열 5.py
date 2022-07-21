def solution():

    N = int(input())
    G = list(map(int, input().split()))

    def find_position(num):
        l = 0
        r = len(graph)

        while l < r:
            mid = (l+r)//2
            if graph[mid] < num:
                l = mid + 1
            else:
                r = mid
        return l

    inf = float("inf")
    route = [1]
    graph = [-inf, G[0]]
    for i in range(1,N):
        x = find_position(G[i])
        if x == len(graph):
            graph.append(G[i])
        route.append(x)
        graph[x] = G[i]


    cnt = max(route)
    print(cnt)
    result = []

    while cnt != 0:
        a = route.pop()
        b = G.pop()
        if a == cnt:
            cnt -= 1
            result.append(b)
    print(*result[::-1])


if __name__ == '__main__':
    solution()
