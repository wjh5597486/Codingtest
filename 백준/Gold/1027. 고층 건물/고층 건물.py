N = int(input())
G = list(map(int,input().split()))

graph = []
for i, value in enumerate(G):
    total_num = 0
    lmax = -float("inf")
    rmax = -float("inf")
    for l, height in enumerate(reversed(G[:i])):
        gradient = (height-value)/(l+1)
        if lmax < gradient:
            lmax = gradient
            total_num += 1

    for r, height in enumerate(G[i+1:]):
        gradient = (height-value)/(r+1)
        if rmax < gradient:
            rmax = gradient
            total_num += 1
    graph.append(total_num)

print(max(graph))