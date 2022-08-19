import copy
import sys
from collections import deque
inf = float("inf")


def solution():
    #첫 째줄: 사람의수, 온라인 서점의 수
    N, M = map(int, sys.stdin.readline().split())
    end = N+M+1

    capacity = [[0] * (N+M+2) for i in range(N+M+2)]
    flow_map = [[0] * (N+M+2) for i in range(N+M+2)]

    #각 사람이 사려고하는 서적의 수
    start_to_custom = list(map(int, sys.stdin.readline().split()))
    for i_custom, num_book in zip(range(1, N+1), start_to_custom):
        capacity[0][i_custom] = num_book

    #셋째 줄에는 각 온라인 서점이 가지고 있는 책의 개수 B1, B2, ..., BM이 주어진다. (1 ≤ Bi ≤ 100)
    store_to_end = list(map(int, sys.stdin.readline().split()))
    for i_store, num_book in zip(range(N+1, N+M+2), store_to_end):
        capacity[i_store][end] = num_book

    #넷째 줄부터 M개의 줄에는 각 온라인 서점이 각 사람들에게 책을 최대 몇 권 팔 수 있는지
    for i_store in range(N+1, M+N+1):
        custom_to_store = list(map(int, sys.stdin.readline().split()))
        for i_custom, num_book in zip(range(1, N+1), custom_to_store):
            capacity[i_custom][i_store] = num_book

    # 그 다음 줄부터 M개의 줄에는 각 온라인 서점이 각 사람들에게 책을 한 권 보내는데 필요한 배송비 Dij가 주어진다.
    cost_map = [[0] * (N+M+2) for i in range(N+M+2)]
    for i_store in range(N+1, N+M+1):
        cost_to_custom = list(map(int, sys.stdin.readline().split()))
        for i_custom, cost in zip(range(1, N+1), cost_to_custom):
            cost_map[i_custom][i_store] = cost
            cost_map[i_store][i_custom] = -cost

    nxt_map = [[]for i in range(N+M+2)]

    for j in range(N + 1, N + M + 1):
        nxt_map[j].append(end)
        for i in range(1, N + 1):
            nxt_map[i].append(j)
            nxt_map[j].append(i)
    for i in range(1, N + 1):
        nxt_map[0].append(i)
        nxt_map[i].append(0)

    def check_flow(start):
        dq = deque([start])
        visited = [0] * (N+M+2)

        while dq:
            cur = dq.popleft()
            visited[cur] = 0
            for nxt in nxt_map[cur]:

                if capacity[cur][nxt] - flow_map[cur][nxt] > 0:
                    cur_cost = cost_checker[cur] + cost_map[cur][nxt]
                    nxt_cost = cost_checker[nxt]

                    if cur_cost < nxt_cost:
                        cost_checker[nxt] = cur_cost
                        flow_checker[nxt] = cur
                        if visited[nxt] == 0:
                            visited[nxt] = 1
                            dq.append(nxt)

    def flow_update(idx):
        nxt = end
        while nxt:
            cur = flow_checker[nxt]
            flow_map[cur][nxt] += 1
            flow_map[nxt][cur] -= 1
            nxt = cur

    cnt = 0
    result = 0
    while True:
        cost_checker = [inf] * (N+M+2)
        cost_checker[0] = 0
        flow_checker = [0] * (N+M+2)

        check_flow(0)
        if cost_checker[-1] != inf:
            flow_update(0)
            cnt += 1
            result += cost_checker[-1]
            continue

        break

    print(cnt)
    # print(result)

if __name__ == '__main__':
    solution()
