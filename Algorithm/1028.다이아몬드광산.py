import sys
input = sys.stdin.readline

N,M = map(int, input().split())

graph = []
for i in range(N):
    text = input()
    graph.append([int(text[i]) for i in range(len(text)-1)])

# for i in graph:print(i)
result = 0


def decrease(r1,c1,r2,c2, i):
    global result
    for x in range(i):
        if r1+x == N or c2-x < 0 or graph[r1+x][c1+x] == 0 or graph[r2+x][c2-x] == 0:
            return 0
    result = max(i, result)
    return 0

def increase(r, c):
    for j in range(750):
        # print(j)
        if r+j == N or c+j ==M or c-j<0:
            break

        if graph[r+j][c-j] == 0 or graph[r+j][c+j] == 0:
            break

        decrease(r+j,c-j,r+j,c+j,1+j)


for r in range(N):
    for c in range(M):
        if graph[r][c] == 1:
            increase(r,c)


print(result)