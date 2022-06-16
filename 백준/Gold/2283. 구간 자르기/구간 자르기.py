import sys
# sys.setrecursionlimit(10**6)

def solution():
    N, K = map(int, input().split())
    left = [0] * 1000010
    right = [0] * 1000010
    for i in range(N):
        l, r = map(int, sys.stdin.readline().split())
        left[l] += 1
        right[r] += 1
    l = 0
    r = 0
    acc = 0
    lnum = left[0]
    rnum = left[0]

    while r<=1000000:
        if acc < K:
            acc += rnum
            r += 1
            rnum -= right[r]
            rnum += left[r]

        elif acc > K:
            acc -= lnum
            l += 1
            lnum -= right[l]
            lnum += left[l]
        else:
            print(l, r)
            return
    print(0, 0)

if __name__ == "__main__":
    solution()
