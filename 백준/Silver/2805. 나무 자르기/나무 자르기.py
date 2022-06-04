from collections import deque

def solution():
    N, M = map(int, input().split())
    G = list(map(int, input().split()))

    left = 1
    right = max(G)

    while left <= right:
        mid = (right + left) // 2

        acc = 0
        for i in G:
            if i > mid:
                acc += i - mid

        if acc >= M:
            left = mid + 1
        else:
            right = mid - 1
    print(right)




if __name__ == "__main__":
    solution()
