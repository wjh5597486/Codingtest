import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())

graph = [[] for __ in range(N + 1)]

for i in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append([cost, b])  # cost destination




def Dijkstra(stt,fin):
    hq = []
    sumCost = [INF] * (N+1)
    heapq.heappush(hq, (0, stt))
    sumCost[stt] = 0

    while hq:
        cost, desti = heapq.heappop(hq)

        for costNext, destiNext in graph[desti]:

            if cost + costNext < sumCost[destiNext]:
                heapq.heappush(hq, (cost + costNext, destiNext))
                sumCost[destiNext] = cost + costNext
    return sumCost[fin]

array = [0] * (N + 1)
for i in range(1, N + 1):
    array[i] = Dijkstra(i, X) + Dijkstra(X, i)
print(max(array))