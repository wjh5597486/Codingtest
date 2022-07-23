def solution():
    import copy
    import itertools

    def find(graph):
        cnt = 0
        for r in range(1,10):
            for c in range(10):
                if graph[r-1][c] == "O":
                    graph = click(graph, r, c)
                    cnt += 1
        return cnt

    def click(graph,r,c):
        for a,b in [[r,c],[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
            if 0<=a<10 and 0<=b<10:
                if graph[a][b] == "O":
                    graph[a][b] = "#"
                else:
                    graph[a][b] = "O"
        return graph

    G = [list(input()) for i in range(10)]
    comb = [list(itertools.combinations(range(10),i)) for i in range(0,11)]
    comb = sum(comb, [])
    result = float("inf")
    for line in comb:
        graph = copy.deepcopy(G)
        for idx in line:
            graph = click(graph,0,idx)
        cnt = find(graph) + len(line)
        if "O" in graph[-1]:
            continue
        else:
            result = min(cnt, result)
    if result == float("inf"):
        print(-1)
    else:
        print(result)


if __name__ == '__main__':
    solution()
