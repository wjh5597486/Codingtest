def solution():
    def check(rr, cc):
        dq = [(rr, cc)]
        graph[rr][cc] = cnt

        while dq:
            r, c = dq.pop()

            for r2, c2 in [[r+1,c],[r,c+1],[r-1,c],[r,c-1]]:
                if 0 <= r2 < N and 0 <= c2 < N:
                    if graph[r2][c2] == 0 and G[r][c] == G[r2][c2]:
                        dq.append((r2, c2))
                        graph[r2][c2] = cnt

    result = []
    N = int(input())
    G = [list(input()) for i in range(N)]
    for i in range(2):
        graph = [[0] * N for i in range(N)]
        cnt = 0
        for c in range(N):
            for r in range(N):
                if graph[r][c] == 0:
                    cnt += 1
                    check(r, c)

        result.append(cnt)

        if len(result) == 1:
            for r in range(N):
                for c in range(N):
                    if G[r][c] == "G":
                        G[r][c] = "R"
    print(*result)

if __name__ == '__main__':
    solution()
