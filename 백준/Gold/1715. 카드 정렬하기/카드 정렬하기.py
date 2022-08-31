import sys
import heapq

def solution():
    G = []
    for i in range(int(input())):
        a = int(sys.stdin.readline())
        heapq.heappush(G, a)

    cnt = 0
    while len(G)-1:
        a = heapq.heappop(G)
        b = heapq.heappop(G)
        c = a + b
        heapq.heappush(G, c)
        cnt += c

    print(cnt)


if __name__ == '__main__':
    solution()
