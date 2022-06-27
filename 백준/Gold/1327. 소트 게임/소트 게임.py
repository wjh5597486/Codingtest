import sys
from collections import deque


def solution():
    N, K = map(int, input().split())
    G = list(map(str, input().split()))
    G = "".join(G)
    S = {G}

    dq = deque()
    dq.append([G, 0])

    while dq:
        item, times = dq.popleft()

        # sort checker
        if list(item) == sorted(list(item)):
            print(times)
            return

        for start in range(N - K + 1):
            end = start + K
            new_item = item[:start] + item[start:end][::-1] + item[end:]

            if new_item not in S:
                S.add(new_item)
                dq.append([new_item, times + 1])

    print(-1)

if __name__ == '__main__':
    solution()
