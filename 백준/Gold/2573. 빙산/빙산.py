import sys
def solution():
    R, C = map(int, sys.stdin.readline().split())
    G = []
    for _ in range(R):
        X = list(map(int, sys.stdin.readline().split()))
        G.append(X)

    def split():
        first = 0
        check = [[0] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if check[r][c] == 0 and G[r][c] != 0:
                    if first == True:
                        return True
                    q = [[r, c]]
                    check[r][c] = 1
                    while q:
                        r1, c1 = q.pop()
                        for r2, c2 in [[r1+1,c1],[r1,c1+1],[r1-1,c1],[r1,c1-1]]:
                            if 0<=r2<R and 0<=c2<C and check[r2][c2]==0 and G[r2][c2]!=0:
                                check[r2][c2] = 1
                                q.append([r2, c2])
                    first = True
        if first == 0:
            return "end"
        return False

    def melt(G):
        G_copy = [i[:] for i in G]
        for r in range(R):
            for c in range(C):
                if G_copy != 0:
                    for r2, c2 in [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]:
                            if 0<=r2<R and 0<=c2<C and G[r2][c2]==0:
                                G_copy[r][c] = max(0, G_copy[r][c]-1)
        return G_copy


    num = 0
    while True:
        result = split()
        if result == True:
            print(num)
            break
        elif result == False:
            G = melt(G)
            num += 1
        elif result == "end":
            print(0)
            break




if __name__ == "__main__":
    solution()

