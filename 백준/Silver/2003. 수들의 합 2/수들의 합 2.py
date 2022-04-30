import sys
def solution():
    N, M = map(int, sys.stdin.readline().split())
    G = list(map(int, sys.stdin.readline().split()))
    L = 0
    R = 0
    nums = G[0]
    result = 0
    try:
        while True:
            if nums > M:
                nums -= G[L]
                L += 1
            else:
                if nums == M:
                    result += 1
                R += 1
                nums += G[R]

    except:
        print(result)


if __name__ == '__main__':
    solution()
