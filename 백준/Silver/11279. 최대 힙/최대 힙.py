from collections import deque
import heapq
import sys
def solution():
    hq = []
    for i in range(int(input())):
        C = int(sys.stdin.readline())
        if C == 0:
            if hq:
                print(-heapq.heappop(hq))
            else:
                print(0)
        heapq.heappush(hq, -C)


if __name__ == '__main__':
    solution()
