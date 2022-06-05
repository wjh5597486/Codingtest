import sys
import heapq
def solution():
    N = int(input())
    left = []
    right = []
    heapq.heappush(left, 10000)
    heapq.heappush(right, 10000)
    for i in range(N):
        N = int(sys.stdin.readline())
        if len(left) == len(right):
            heapq.heappush(left, -N)
        else:
            heapq.heappush(right, N)

        if -left[0] > right[0]:
            l = -heapq.heappop(left)
            r = heapq.heappop(right)
            heapq.heappush(left, -r)
            heapq.heappush(right, l)


        print(-left[0])
if __name__ == "__main__":
    solution()
