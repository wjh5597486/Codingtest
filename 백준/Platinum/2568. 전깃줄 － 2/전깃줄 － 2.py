from collections import deque
import sys

def solution():
    G = []
    N = int(input())
    for i in range(N):
        r, c = map(int, sys.stdin.readline().split())
        G.append((r,c))
    G.sort(key=lambda x:x[1])
    G = list(map(lambda x: x[0], G))

    lows = [0,G[0]]

    def low_bound(num):
        l = 0
        r = len(lows)-1
        if lows[-1] < num:
            return r+1
        while l < r:
            mid = (l+r)//2
            if lows[mid] < num:
                l = mid + 1
            else:
                r = mid
        return r

    result = [1]
    for i in G[1::]:
        index = low_bound(i)
        result.append(index)

        if index == len(lows):
            lows.append(i)
        elif i < lows[index]:
            lows[index] = i

    cnt = max(result)
    S = set()
    for i in range(len(result)-1,-1,-1):
        if result[i] == cnt:
            S.add(G[i])
            cnt -= 1

    print(len(G) - len(S))
    for i in sorted(G):
        if i in S:
            continue
        else:
            print(i)



if __name__ == '__main__':
    solution()
