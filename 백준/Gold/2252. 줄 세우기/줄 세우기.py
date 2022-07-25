from collections import deque
import sys

def solution():

    N, M = map(int, input().split())
    num_edge = [0 for _ in range(N+1)]
    subsequence = [[] for _ in range(N+1)]

    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        num_edge[b] += 1
        subsequence[a].append(b)

    S = [i for i in range(1, N+1) if num_edge[i] == 0]
    q = deque(S)

    result = []
    while q:
        a = q.popleft()
        result.append(a)
        for idx in subsequence[a]:
            num_edge[idx] -= 1
            if num_edge[idx] == 0:
                q.append(idx)
    print(*result)




if __name__ == '__main__':
    solution()
