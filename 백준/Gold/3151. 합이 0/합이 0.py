import sys

def solution():
    N = int(sys.stdin.readline())
    G = list(map(int, sys.stdin.readline().split()))
    G.sort()

    result = 0

    for i in range(N-2):
        if G[i] > 0:
            break
        L = i + 1
        R = N - 1

        while L < R:
            value = G[i] + G[L] + G[R]

            if value > 0:
                R -= 1

            elif value < 0:
                L += 1

            else:
                if G[L] == G[R]:
                    result += (R - L + 1) * (R - L) // 2
                    break

                else:
                    r = 0
                    while G[R] == G[R-r]:
                        r += 1
                    R -= r

                    l = 0
                    while G[L] == G[L+l]:
                        l += 1
                    L += l
                    result += l * r
    print(result)

if __name__ == '__main__':
    solution()
