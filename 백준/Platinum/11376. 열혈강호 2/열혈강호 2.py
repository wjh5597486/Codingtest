import sys

def solution():
    N, M = map(int, input().split())
    G = [list(map(int, sys.stdin.readline().split()))[1::] for i in range(N)]
    Q = [-1] * (M+1)

    def dfs(idx):
        if check[idx] == 1:
            return False
        check[idx] = 1

        for i in G[idx]:

            if Q[i] == -1 or dfs(Q[i]):
               Q[i] = idx
               return True

        return False

    for _ in range(2):
        for i in range(N):
            check = [-1] * (N+1)
            dfs(i)

    print(sum(1 if i != -1 else 0 for i in Q))

if __name__ == '__main__':
    solution()