import sys
sys.setrecursionlimit(10**4)

def solution():
    N = int(input())
    G = [0] + list(map(int, input().split()))
    M = int(input())

    # tree_m = [0] * (N*4)
    tree_t, tree_r, tree_l, tree_m = [[0] * (N*4) for _ in range(4)]

    def init(left=1, right=N, idx=1):
        if left == right:
            tree_t[idx] = G[left]
            tree_l[idx] = tree_r[idx] = tree_m[idx] = max(G[left], 0)
        else:
            mid = (left + right) // 2
            L_l, L_t, L_r, L_m = init(left, mid, idx*2)
            R_l, R_t, R_r, R_m = init(left, mid, idx*2)
            tree_t[idx] = L_t + R_t
            tree_l[idx] = max(L_l, L_t + R_l)
            tree_r[idx] = max(R_r, R_t + L_r)
            tree_m[idx] = max(L_r + R_l, L_l, R_r, L_m, R_m)

        return tree_l[idx], tree_t[idx], tree_r[idx], tree_m[idx]


    def get_item(cls, left, right, start=1, end=N, idx=1):
        if right < start or end < left:
            return 0

        if left <= start and end <= right:
            if cls == "left":
                return tree_l[idx]
            elif cls == "right":
                return tree_r[idx]
            else:
                return tree_t[idx]
        else:
            mid = (start + end) // 2
            return get_item(cls, left, right, start, mid, idx*2) +\
                   get_item(cls, left, right, mid+1, end, idx*2+1)


    def get_total(left, right, start=1, end=N, idx=1):
        if right < start or end < left:
            return 0

        if left <= start and end < right:
            return tree_t[idx]

        else:
            mid = (start + end) // 2
            return get_total(left, right, start, mid, idx*2) + get_total(left, right, mid+1, end, idx*2+1)


    def get_left(left, right, start=1, end=N, idx=1):
        ...
    def get_right(left, right, start=1, end=N, idx=1):
        ...
    init()
    print(tree_t)
    print(tree_r)
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())

        """
        case 1)         
        x1 ----- y1
                     x2 ----- y2
                     
        case2)         
        x1 ----- y1
             x2 ----- y2
             
             get_mid(x2-y1)
        """

        if y1 <= x2:
            print(get_right(x1, y1-1) + get_total(y1, x2) + get_left(x2+1, y2))

        else:
            print(get_right(x1, y1) + get_left(x2, y2) - get_total(y1, x2))


if __name__ == '__main__':
    solution()
