from collections import deque
import sys

def solution():
    N = int(input())

    G = list(map(int, sys.stdin.readline().split()))
    graph = [0]*(N+1)
    for idx, num in zip(range(1,N+1), G):
        graph[num] = idx


    K = list(map(int, input().split()))

    result = [-1]

    def BS(idx):
        if result[-1] < idx:
            result.append(idx)
            return len(result)-1

        l = 0
        r = len(result)
        while l<r:
            mid = (l+r) // 2
            if result[mid] < idx:
                l = mid + 1
            else:
                r = mid
        return l

    for num in K:
        position = graph[num]
        result[BS(position)] = position

    print(len(result[1::]))


if __name__ == '__main__':
    solution()
