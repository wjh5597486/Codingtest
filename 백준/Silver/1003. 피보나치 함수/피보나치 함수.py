import sys
# sys.setrecursionlimit(10**6)
def solution():
    G = [[1, 0], [0, 1]]
    for i in range(3,40+2):
        G.append([G[-1][0]+G[-2][0], G[-1][1]+G[-2][1]])

    for i in range(int(input())):
        print(*G[int(sys.stdin.readline())])

if __name__ == "__main__":
    solution()
