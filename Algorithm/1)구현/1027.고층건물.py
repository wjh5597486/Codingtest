N = 5

graph = [1,2,3,4,5]

G = [0] * N
for i, st in enumerate(graph):
    for j, di in enumerate(graph[i::]):
        print(i, i + j + 1)
        G(st - di)/(j - i)