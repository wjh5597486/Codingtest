N = int(input())
graph = [1, 3, 5]
for i in range(3, N):
    graph.append((graph[-2]*3 + graph[-3]*2) % 10007)
print(graph[N-1])