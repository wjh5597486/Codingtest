# https://www.acmicpc.net/problem/15961
import sys
from collections import defaultdict

def solution():
    N, _, M, num = map(int, sys.stdin.readline().split())
    G = [int(sys.stdin.readline()) for _ in range(N)]

    if N != M:
        G = G + G[:M]

    l = 0
    r = l + M - 1

    result = 0
    cur_sum = defaultdict(int)
    for i in range(M):
        cur_sum[G[i]] += 1
    cur_sum[num] += 1

    while r < len(G)-1:
        result = max(cur_sum.__len__(), result)
        l += 1
        r += 1
        cur_sum[G[l - 1]] -= 1
        if cur_sum[G[l-1]] == 0:
            del cur_sum[G[l-1]]
        cur_sum[G[r]] += 1

    print(result)


if __name__ == '__main__':
    solution()
