import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize


N = int(input()) + 1
M = int(input())

route = [[] for __ in range(N)]
sumCost = [INF] * N

for __ in range(M):
    x, y, c = map(int, input().split())
    route[x].append([c, y]) # [cost, destination]

stt, fin = map(int, input().split())

def go():
    hq = []
    sumCost[stt] = 0
    heapq.heappush(hq, (0, stt))  # cost, point

    while hq:
        cost, point = heapq.heappop(hq)

        if cost > sumCost[point]:
            continue

        for next_cost, y in route[point]:
            if cost + next_cost < sumCost[y]:
                sumCost[y] = cost + next_cost
                heapq.heappush(hq, (cost + next_cost, y))
go()
if sumCo
print(sumCost[fin])


