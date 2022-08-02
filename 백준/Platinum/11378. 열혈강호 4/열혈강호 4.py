import sys

def solution():
    N, M, K = map(int, input().split())
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


    cnt = 0
    for i in range(N):
        check = [-1] * (N+1)
        cnt += dfs(i)

    for i in range(N):
        while K > 0:
            check = [-1] * (N + 1)
            if dfs(i):
                K -= 1
                cnt += 1
            else:
                break

    print(cnt)



if __name__ == '__main__':
    solution()