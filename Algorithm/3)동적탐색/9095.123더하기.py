graph = [1,1,2]

def D(N):
    while len(graph) < N+1:
        X=len(graph)
        graph.append(graph[-3]+graph[-2]+graph[-1])
    print(graph[N])

for i in range(int(input())):
    D(int(input()))
