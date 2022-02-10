import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize


N, M = map(int, input().split())
N += 1

route = [[] for __ in range(N)]

for __ in range(M):
    x, y, c = map(int, input().split())
    route[x].append([c, y]) # [cost, destination]
    route[y].append([c, x]) # [cost, destination]

node1, node2 = map(int, input().split())

def go(stt, fin):
    hq = []
    sumCost = [INF] * N
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
    return sumCost[fin]

X = go(1, node1) + go(node1, node2) + go(node2, N-1)
Y = go(1, node2) + go(node2, node1) + go(node1, N-1)
X = min(X, Y)

if X >= INF:
    print(-1)
else:
    print(X)


