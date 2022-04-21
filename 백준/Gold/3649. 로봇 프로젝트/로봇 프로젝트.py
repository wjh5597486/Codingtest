import sys
def solution():
    input = sys.stdin.readline
    X = int(input())*10000000
    G = [int(input()) for _ in range(int(input()))]
    G.sort()
    L = 0
    R = len(G)-1

    while L < R:
        sum = G[L] + G[R]
        if sum > X:
            R -= 1
        elif sum < X:
            L += 1
        else:
            print("yes %d %d" %(G[L], G[R]))
            return

    print("danger")

if __name__ == '__main__':
    while True:
        try:
            solution()
        except:
            break