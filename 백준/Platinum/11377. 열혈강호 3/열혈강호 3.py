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

    for _ in range(2):
        for i in range(N):
            check = [-1] * (N+1)
            dfs(i)
    dic = {}
    cnt = 0
    for i in range(1, M+1):
        if Q[i] != -1:
            if dic.get(Q[i]) == None:
                dic[Q[i]] = 1
                cnt += 1
                continue
            elif K != 0:
                dic[Q[i]] += 1
                K -= 1
                cnt += 1
                continue
    print(cnt)

    # print(sum(1 if i != -1 else 0 for i in Q))

if __name__ == '__main__':
    solution()