def solution():
    N = int(input())
    a, b = map(int, input().split())
    G = [[] for i in range(N+1)]
    for i in range(int(input())):
        x, y = map(int, input().split())
        G[x].append(y)
        G[y].append(x)

    q = [(a, 0)]
    check = [-1] * (N+1)

    while q:
        cur, cnt = q.pop()

        for nxt in G[cur]:
            if check[nxt] != -1:
                continue
            check[nxt] = cnt + 1
            q.append((nxt, cnt+1))
    print(check[b])


if __name__ == "__main__":
    solution()
