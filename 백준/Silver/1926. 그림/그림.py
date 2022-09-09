import sys
def solution():
    result = 0
    R, C = map(int, input().split())
    G = [list(map(int, input().split())) for i in range(R)]
    cnt = 0
    result = 0
    size = 0
    for r in range(R):
        for c in range(C):
            if G[r][c] == 1:
                cnt += 1
                q = [(r,c)]
                size = 1
                G[r][c] = 0
                while q:
                    r1, c1 = q.pop()
                    for r2, c2 in [[r1+1, c1], [r1, c1+1],
                                   [r1-1, c1], [r1, c1-1]]:
                        if 0<=r2<R and 0<=c2<C:
                            if G[r2][c2] == 1:
                                size += 1
                                q.append((r2, c2))
                                G[r2][c2] = 0
                result = max(size, result)
    print(cnt)
    print(result)

if __name__ == '__main__':
    solution()
