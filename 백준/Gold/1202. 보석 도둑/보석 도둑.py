import heapq
import sys
def solution():
    N, K = map(int, input().split())
    jewel = []
    for i in range(N):
        jewel.append(tuple(map(int, sys.stdin.readline().split())))

    jewel.sort(key=lambda x: [-x[0], x[1]])

    bags = []
    for i in range(K):
        bags.append(int(sys.stdin.readline()))
    bags.sort()

    cnt = 0

    hq = []
    for max_weight in bags:
        while jewel and jewel[-1][0] <= max_weight:
            weight, cost = jewel.pop()
            heapq.heappush(hq, -cost)
        if hq:
            value = heapq.heappop(hq)
        else:
            value = 0
        cnt -= value

    print(cnt)


if __name__ == '__main__':
    solution()
