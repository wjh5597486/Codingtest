import sys
from heapq import heappush, heappop

input = sys.stdin.readline
inf = sys.maxsize

n, m, k = map(int, input().split())
graph =[[] for _ in range(n + 1)]
dp = [[inf] * k for _ in range(n + 1)]
heap = []

def dijkstra(start):
    heappush(heap, [0, start])
    dp[start][0] = 0
    while heap:
        cost, cur_point = heappop(heap)
        for next_point, wei in graph[cur_point]:
            next_cost = wei + cost
            if next_cost < dp[next_point][k-1]:
                dp[next_point][k-1] = next_cost
                dp[next_point].sort()
                heappush(heap, [next_cost, next_point])

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

dijkstra(1)

for i in range(1, n + 1):
    if dp[i][k-1] == inf:
        print(-1)
    else:
        print(dp[i][k-1])