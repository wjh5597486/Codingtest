import sys
sys.setrecursionlimit(10**5)
def solution():
    N = int(input())
    G = [list(map(int, input().split())) for i in range(N)]
    R = [[0] * N for i in range(N)]

    def check(r, c):
        if R[r][c] != 0:
            return R[r][c]

        max_adj = 0
        for r2, c2 in [[r+1, c],[r, c+1],[r-1, c],[r, c-1]]:
            if 0 <= r2 < N and 0 <= c2 < N:
                if G[r][c] > G[r2][c2]:
                    max_adj = max(max_adj, check(r2, c2))


        R[r][c] = max_adj+1

        return R[r][c]

    for r in range(N):
        for c in range(N):
            check(r, c)

    print(max(map(max, R)))

if __name__ == '__main__':
    solution()
