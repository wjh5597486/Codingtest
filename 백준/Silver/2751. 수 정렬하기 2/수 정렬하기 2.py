import sys
def solution():
    G = [int(sys.stdin.readline()) for i in range(int(input()))]
    G.sort()
    for i in G:print(i)

if __name__ == '__main__':
    solution()