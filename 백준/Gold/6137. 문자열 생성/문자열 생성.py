import sys


def solution():
    N = int(input())
    G = []
    for i in range(N):
        G.append(sys.stdin.readline().rstrip())
    L = 0
    R = N-1
    result = ""
    while L <= R:
        if G[L] < G[R]:
            result += G[L]
            L += 1
        elif G[R] < G[L]:
            result += G[R]
            R -= 1
        elif L!=R: # the same
            l, r = "", ""
            for i in range(1000000):
                l += G[L+i]
                r += G[R-i]
                if l > r:
                    result += G[R]
                    R -= 1
                    break
                elif r > l:
                    result += G[L]
                    L += 1
                    break
                elif L+i == N or R-i <0 or L+i > R-i:
                    result += G[L]
                    L += 1
                    break
        else:
            result += G[L]
            break
        if len(result) == 80:
            print(result)
            result = ""

    print(result)



if __name__ == "__main__":
    solution()
