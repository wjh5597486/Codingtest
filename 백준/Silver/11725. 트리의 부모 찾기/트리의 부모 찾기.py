def solution():

    N = int(input())
    G = [[] for i in range(N+1)]
    for i in range(N-1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    graph = [-1] * (N+1)
    q = [1]
    while q:
        parent = q.pop()
        for child in G[parent]:
            if graph[child] == -1:
                graph[child] = parent
                q.append(child)

    for i in graph[2::]:
        print(i)




if __name__ == '__main__':
    solution()
