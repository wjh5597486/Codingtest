###???? 이게된다고??
def solution():
    import sys

    def dfs(cur):
        visit[cur] = 1
        for nxt in graph[cur]:
            if (b[nxt] == -1) or (not visit[b[nxt]] and dfs(b[nxt])):
                b[nxt] = cur
                return 1
        return 0

    n = int(sys.stdin.readline())
    shark = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                if shark[i] == shark[j]:
                    graph[min(i, j)].append(max(i, j))

                elif (shark[i][0] >= shark[j][0]) and (shark[i][1] >= shark[j][1]) and (shark[i][2] >= shark[j][2]):
                    graph[i].append(j)

    b = [-1] * n
    ans = 0

    for i in range(2 * n):
        visit = [0] * n
        ans += dfs(i // 2)

    print(n - ans)

if __name__ == '__main__':
    solution()
