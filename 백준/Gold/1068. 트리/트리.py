def solution():
    N = int(input())
    graph = list(map(int, input().split()))

    deleted = int(input())

    G = [[] for _ in range(N)]

    for idx, parent in enumerate(graph):
        if parent == -1:
            root = idx
        elif idx != deleted:
            G[parent].append(idx)
    G[deleted] = []

    result = 0
    q = [root]
    while q:
        parents = q.pop()
        if G[parents] == [] and parents is not deleted:
            result += 1
        else:
            q += G[parents]

    print(result)





if __name__ == "__main__":
    solution()
