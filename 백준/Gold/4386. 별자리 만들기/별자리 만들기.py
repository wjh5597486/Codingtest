import math
def solution():
    N = int(input())
    V = list(range(N+1))
    graph = []

    for i in range(N):
        graph.append(list(map(float, input().split())))
    E = []
    for i in range(N-1):
        for j in range(i+1, N):
            E.append((math.dist(graph[i],graph[j]), i, j ))
    E.sort()

    def find(idx):
        if idx != V[idx]:
            V[idx] = find(V[idx])
        return V[idx]

    cnt = 0
    for c, a, b in E:
        v_a = find(a)
        v_b = find(b)
        if v_a != v_b:
            V[max(v_a,v_b)] = min(v_a, v_b)
            cnt += c

    print(round(cnt,2))

if __name__ == '__main__':
    solution()
