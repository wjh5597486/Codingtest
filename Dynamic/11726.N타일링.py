N = int(input())
graph = [1, 2, 3]
for i in range(3, N):
    graph.append((graph[-2]*2 + graph[-3]) % 10007)
print(graph[N-1])