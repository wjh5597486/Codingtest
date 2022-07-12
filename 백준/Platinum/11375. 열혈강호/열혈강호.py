import sys
sys.setrecursionlimit(1_000_000)

def solution():
    N, M = map(int, input().split())
    G = [list(map(int, sys.stdin.readline().split()))[1::] for i in range(N)]
    job = [-1]*(M+1)

    def dfs(idx):
        job_list = G[idx]
        for job_idx in job_list:
            if check[job_idx] != -1:
                continue
            check[job_idx] = 1

            if job[job_idx] == -1 or dfs(job[job_idx]):
                job[job_idx] = idx
                return True
        return False


    for idx in range(N):
        check = [-1] * (M+1)
        dfs(idx)

    print(sum(1 if i != -1 else 0 for i in job))

if __name__ == '__main__':
    solution()