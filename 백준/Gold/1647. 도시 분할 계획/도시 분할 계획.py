def solution():
    N, M = map(int,input().split())
    V = list(range(N+1))
    E = []
    for i in range(M):
        E.append(list(map(int, input().split())))
    E.sort(key=lambda x:x[2])
    cnt = 0

    def find(idx):
        if V[idx] != idx:
            V[idx] = find(V[idx])
        return V[idx]

    num_edge = 0
    for a,b,c in E:
        v_a = find(a)
        v_b = find(b)
        if v_a != v_b:
            V[max(v_a, v_b)] = V[min(v_a, v_b)]
            cnt += c
            num_edge += 1
        if num_edge == N-2:
            print(cnt)
            return
if __name__ == '__main__':
    solution()
