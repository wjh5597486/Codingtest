import heapq

N, D = map(int, input().split())

l = [[[1, i+1]] for i in range(10001)]
for i in range(N):
    s, f, c = map(int, input().split())
    l[s].append([c, f])  # cost, next

hq = []
heapq.heappush(hq, (0, 0))  # start cost 0, position 0

INF = float("inf")
COST = [INF] * 10001

while hq:
    cost, stt = heapq.heappop(hq)
    for cost_route, next_p in l[stt]:
        if COST[next_p] > cost_route + cost and next_p <= D:
            heapq.heappush(hq, (cost_route + cost, next_p))  # start cost 0, position 0
            COST[next_p] = cost_route + cost

print(COST[D])