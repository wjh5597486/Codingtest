import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

N, M, K = map(int, input().split())
N += 1
stt = 1

route = [[] for __ in range(N)]
sumCost = [INF] * N

for __ in range(M):
    x, y, c = map(int, input().split())
    route[x].append([c, y])  # [cost, destination]



short = [[] for __ in range(N)]
short[1].append(0)

def go():
    hq = []
    sumCost[stt] = 0
    heapq.heappush(hq, (0, stt))  # cost, point

    while hq:
        cost, point = heapq.heappop(hq)
        for next_cost, y in route[point]:
            if len(short[y]) < K:

                short[y].append(cost + next_cost)
                sumCost[y] = cost + next_cost
                heapq.heappush(hq, (cost + next_cost, y))


    for L in short[1::]:
        if len(L) < K:
            print(-1)
        else:
            print(sorted(L)[-1])
go()