from collections import deque
import sys

def solution():
    R, C = map(int, input().split())
    G = []
    for i in range(R):
        line = sys.stdin.readline().strip()
        G.append(list(map(lambda x: int(x), line)))

    diction = dict()
    diction[0] = 0
    def count(r,c):
        cnt = 0
        dq = deque()
        dq.append([r,c])
        sector[r][c] = sector_idx
        while dq:
            r, c = dq.popleft()
            cnt += 1
            for r2, c2 in [[r+1,c],[r,c+1],[r-1,c],[r,c-1]]:
                if 0<=r2<R and 0<=c2<C:
                    if sector[r2][c2] == 0 and G[r2][c2] == 0:
                        sector[r2][c2] = sector_idx
                        dq.append([r2,c2])
        diction[sector_idx] = cnt

    graph = [[0] * C for _ in range(R)]
    sector = [[0] * C for _ in range(R)]
    sector_idx = 1
    for r in range(R):
        for c in range(C):
            if G[r][c] == 0 and sector[r][c] == 0:
                count(r, c)
                sector_idx += 1



    result = [""] * R
    for r in range(R):
        for c in range(C):
            S = set()
            cnt = 1
            if G[r][c] == 1:
                for r2, c2 in [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]:
                    if 0 <= r2 < R and 0 <= c2 < C:
                        if sector[r2][c2] in S:
                            continue
                        else:
                            S.add(sector[r2][c2])
                            cnt += diction[sector[r2][c2]]

                result[r] += str(cnt%10)
            else:
                result[r] += str(0)

    for i in result:
        print(i)



if __name__ == '__main__':
    solution()
