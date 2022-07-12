import sys
sys.setrecursionlimit(1_000_000)
import math
def solution():
    N = int(input())
    G = list(map(int, input().split()))

    def isprime(num):
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True

    graph_origin = [[] for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1,N):
            number = G[i] + G[j]
            if isprime(number) == True:
                graph_origin[i].append(j)
                graph_origin[j].append(i)


    def dfs(idx):
        for i in graph[idx]:

            if check[i] == 1:
                continue
            check[i] = 1

            if Q[i] == -1 or dfs(Q[i]):
                Q[i] = idx
                Q[idx] = i
                check[idx] = 1
                check[idx] = 1
                return True

        return False


    result = []
    for x1 in graph_origin[0]:
        graph = graph_origin.copy()
        for line in graph[1::]:
            if x1 in line:
                line.pop(line.index(x1))

        Q = [-1] * N
        Q[0] = x1
        Q[x1] = 0

        for i in range(1, N):
            check = [0] * N
            check[0] = 1
            check[x1] = 1
            if Q[i] == -1:
                dfs(i)

        if -1 not in Q:
            result.append(G[Q[0]])


    result.sort()
    
    if result == []:
        print(-1)
    else:
        print(*result)





if __name__ == '__main__':
    solution()