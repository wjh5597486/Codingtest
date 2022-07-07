def solution():
    from collections import deque
    R, C = map(int, input().split())
    G = []
    for i in range(R):
        G.append(list(input()))
    result = 0

    for i in range(R):
        for j in range(C):

            if G[i][j] == "W":
                continue

            check = 0
            for r2, c2 in [[i+1, j],[i, j+1],[i-1, j],[i, j-1]]:
                if 0 <= r2 < R and 0 <= c2 < C:
                    if G[r2][c2] == "L":
                        check += 1
            if check > 2:
                continue


            visit = [[-1] * C for _ in range(R)]
            dq = deque()
            dq.append([i, j])
            visit[i][j] = 0
            while dq:
                r, c = dq.popleft()
                for r2, c2 in [[r+1, c],[r, c+1],[r-1, c],[r, c-1]]:
                    if 0 <= r2 < R and 0 <= c2 < C:
                        if visit[r2][c2] == -1 and G[r2][c2] == "L":
                            visit[r2][c2] = visit[r][c] + 1
                            dq.append([r2, c2])
                            result = max(visit[r2][c2], result)

    print(result)



if __name__ == '__main__':
    solution()
