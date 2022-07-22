def solution():
    V, E = map(int, input().split())
    v_root = [i for i in range(V+1)]
    G = []
    for i in range(E):
        a,b,c = map(int, input().split())
        G.append((c,a,b))

    G.sort()

    def find(idx):
        if idx != v_root[idx]:
            v_root[idx] = find(v_root[idx])
        return v_root[idx]

    cnt = 0
    for cost, a, b in G:
        
        a_root = find(a)
        b_root = find(b)

        if a_root != b_root:
            if a_root > b_root:
                v_root[a_root] = b_root
            else:
                v_root[b_root] = a_root
            cnt += cost

    print(cnt)

if __name__ == '__main__':
    solution()
