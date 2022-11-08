from collections import deque
def solution():
    inf = float("inf")
    for round in range(1, 1000):
        N = int(input())
        if N == 0:
            break
        G = [list(map(int, input().split())) for _ in range(N)]
        check = [[inf] * N for i in range(N)]
        dq = deque()
        dq.append((0, 0, G[0][0]))
        check[0][0] = G[0][0]
        while dq:
            r, c, cnt = dq.popleft()
            for r2, c2 in [[r-1,c],[r+1,c],[r,c-1],[r,c+1]]:
                if 0<=r2<N and 0<=c2<N:
                    if check[r2][c2] > check[r][c] + G[r2][c2]:
                        dq.append((r2, c2, check[r][c] + G[r2][c2]))
                        check[r2][c2] = check[r][c] + G[r2][c2]
        print(f"Problem {round}: {check[-1][-1]}")

if __name__ == "__main__":
    solution()
