import sys
sys.setrecursionlimit(10**5)
def solution():
    for i in range(int(sys.stdin.readline())):
        V, E = map(int, sys.stdin.readline().split())

        G = [[] for i in range(V+1)]

        for i in range(E):
            a, b = map(int, sys.stdin.readline().split())
            G[a].append(b)
            G[b].append(a)

        group = [0] * (V+1)
        group[0] = 1

        def check(cur):
            for nxt in G[cur]:
                if group[nxt] == 0:
                    group[nxt] = -group[cur]
                    if check(nxt) == False:
                        return False

                elif group[cur] == group[nxt]:
                    return False

            return True

        result = True

        for i in range(1, V+1):
            if group[i] == 0:
                group[i] = 1
                if check(i) == 0:
                    result = False
                    break

        if result:
            print("YES")
        else:
            print("NO")






if __name__ == '__main__':
    solution()
