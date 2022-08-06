def solution():
    N, a1, a2, a3, a4 = map(int, input().split())
    prob = list(map(lambda x: x/100, [a1, a2, a3, a4]))

    def dfs(cnt, mass, r, c, S):
        if cnt == N:
            nonlocal success
            success += mass
            return

        for (r2, c2), p in zip([[r+1,c],[r-1,c],[r,c+1],[r,c-1]], prob):
            if prob == 0:
                continue

            if (r2, c2) not in S:
                g = S.copy()
                g.add((r2,c2))
                dfs(cnt+1, p * mass, r2, c2, g)


    success = 0
    dfs(0, 1, 0, 0, set([(0,0)])) # cnt, mass, r, c, set

    print(success)


if __name__ == '__main__':
    solution()