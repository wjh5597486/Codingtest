from collections import deque
import heapq
import sys
def solution():

    N, M = map(int, input().split())
    dq = deque()
    dq.append((N,1))
    while dq:
        n, c = dq.popleft()
        if n == M:
            print(c)
            return
        for n2 in [n*10+1, n*2]:
            if n2 <= M:
                dq.append((n2, c+1))
    print(-1)
if __name__ == '__main__':
    solution()
