import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize


N, M, final_cost, stt = map(int, input().split())
N += 1

route = [[] for __ in range(N)]
sumCost = [INF] * N

for __ in range(M):
    x, y = map(int, input().split())
    route[x].append([1, y]) # [cost, destination]


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
if final_cost in sumCost:
    for index, x in enumerate(sumCost):
        if x == final_cost:
            print(index)
else:
    print(-1)


