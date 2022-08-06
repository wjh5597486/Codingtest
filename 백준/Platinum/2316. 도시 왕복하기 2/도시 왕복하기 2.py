import copy
def solution():
    N, M = map(int, input().split())
    capacity = [[0] * (N+1) for i in range(N+1)]
    flow = copy.deepcopy(capacity)

    for i in range(M):
        a, b = map(int, input().split())
        capacity[a][b] = 1
        capacity[b][a] = 1

    def flow_check(start, end):
        q = [start]

        while q:
            a = q.pop()

            if a == end:
                return True

            for idx in range(1, N+1):
                if capacity[a][idx] - flow[a][idx] > 0:
                    if check[idx] == -1:
                        check[idx] = a
                        q.append(idx)

        return False


    def flow_add(start, end):
        prior = end
        graph = [-1] * (N+1)
        while prior != start:
            posterior = check[prior]
            flow[posterior][prior] += 1
            flow[prior][posterior] -= 1
            graph[posterior] = 1
            prior = posterior
        return graph

    cnt = 0

    check = [-1] * (N + 1)
    while True:
        if flow_check(1, 2):
            check = flow_add(1, 2)

            cnt += 1

        else:
            break
    print(cnt)



if __name__ == '__main__':
    solution()