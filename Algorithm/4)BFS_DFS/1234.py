import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())

heap = []
graph = [[] for _ in range(n + 1)]

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append([y, z])

INF = sys.maxsize
value = [INF] * (n + 1)
value[k] = 0

heapq.heappush(heap, (0, k))

while heap:
    dist, now = heapq.heappop(heap)
    for q, w in graph[now]:
        if dist + w < value[q]:
            value[q] = dist + w
            heapq.heappush(heap, (dist + w, q))

for i in range(1, n + 1):
    if value[i] == INF:
        print("INF")
    else:
        print(value[i])