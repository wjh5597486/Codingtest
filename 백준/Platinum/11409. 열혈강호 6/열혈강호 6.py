import copy
import sys
from collections import deque
inf = float("inf")


def solution():
    N, M = map(int, input().split())
    graph = [[] for i in range(N + M + 2)]
    cost_map = [[0] * (N+M+2) for i in range(N + M + 2)]

    for idx_mem in range(1, N + 1):
        line = list(map(int, sys.stdin.readline().split()))
        for i in range(line[0]):
            item_num = line[i * 2 + 1] + N
            item_value = line[i * 2 + 2]
            graph[idx_mem].append(item_num)
            cost_map[idx_mem][item_num] = -item_value
            cost_map[item_num][idx_mem] = +item_value

    for i in range(1, N + 1):  # start to member
        graph[0].append(i)

    for i in range(N + 1, N + M + 1):  # item to end
        graph[i].append(N+M+1)
    c = 0
    def flow_check(start, end):
        dq = deque()
        dq.append(start)  # cur_idx, cur_cost

        while dq:
            cur_idx = dq.popleft()
            visited[cur_idx] = 0

            for nxt_idx in graph[cur_idx]:
                cur_cost = cost_checker[cur_idx]
                nxt_cost = cost_map[cur_idx][nxt_idx]
                if cost_checker[nxt_idx] > nxt_cost + cur_cost:
                    cost_checker[nxt_idx] = nxt_cost + cur_cost
                    flow_checker[nxt_idx] = cur_idx
                    if not visited[nxt_idx]:
                        dq.append(nxt_idx)
                        visited[nxt_idx] = 1

        if cost_checker[-1] == inf:
            return False

        else:
            return True

    def flow_update(first, last):
        nonlocal result

        posterior = first
        while posterior != last:
            prior = flow_checker[posterior]
            result += cost_map[prior][posterior]
            graph[prior].remove(posterior)
            graph[posterior].append(prior)
            posterior = prior

    cnt = 0
    result = 0
    for i in range(N):

        cost_checker = [inf] * (N + M + 2)
        cost_checker[0] = 0
        flow_checker = [-1] * (N + M + 2)
        visited = [0] * (N+M+2)

        if flow_check(0, N + M + 1):
            flow_update(N + M + 1, 0)
            cnt += 1

        else:
            break

    print(cnt)
    print(-result)
if __name__ == '__main__':
    solution()
