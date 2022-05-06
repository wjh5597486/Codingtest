import sys

def solution():
    N = int(input())
    G = []
    for i in range(N):
        G.append(int(sys.stdin.readline()))

    G.sort()

    temp = []
    for i in range(0, N):
        cnt = 0
        for j in range(G[i], G[i]+5):
            if j not in G:
                cnt +=1
        temp.append(cnt)
    print(min(temp))



if __name__ == '__main__':
    solution()
