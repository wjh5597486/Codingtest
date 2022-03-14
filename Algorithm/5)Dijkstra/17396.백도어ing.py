import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
G = list(map(int, input().split()))
graph = [[] for __ in range(N)]
G[N-1] = 0

for i in range(M):
    x, y, c = map(int, input().split())
    if G[y] == 0 and G[x] == 0:
        graph[x].append([y, c])  # goal, cost
        graph[y].append([x, c])  # goal, cost


hq = []
heapq.heappush(hq, [0, 0])
INF = float("inf")
cost_list = [INF] * N

result = -1

while hq:
    cost_sum, start = heapq.heappop(hq)
    if start == N-1:
        result = cost_list[-1]
        break

    for goal, cost in graph[start]:
        if cost_list[goal] > cost_sum + cost:
            heapq.heappush(hq, [cost_sum + cost, goal])
            cost_list[goal] = cost_sum + cost

print(result)