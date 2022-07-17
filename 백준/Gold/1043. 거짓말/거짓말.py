def solution():
    N, M = map(int, input().split())
    member = list(map(int, input().split()))[1::]
    graph = [[0] * 51 for i in range(51)]
    G = []
    for i in range(M):
        data = list(map(int, input().split()))[1::]
        G.append(set(data))
        for i in range(len(data)):
            for j in range(i, len(data)):
                graph[data[i]][data[j]] = 1
                graph[data[j]][data[i]] = 1
    check = [0] * 51
    for i in member:
        check[i] = 1
    result = []
    while member:
        a = member.pop()
        result.append(a)
        for idx, b  in enumerate(graph[a]):
            if b == 1 and check[idx] == 0:
                member.append(idx)
                check[idx] = 1

    cnt = M
    for party in G:
        for mem in result:
            if mem in party:
                cnt -= 1
                break
    print(cnt)




if __name__ == '__main__':
    solution()