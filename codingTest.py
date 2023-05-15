import bisect
import sys
sys.setrecursionlimit(10**4)
inf = float("inf")


def solution():
    N = int(input())
    G = [0] + list(map(int, input().split()))
    M = int(input())

    tree_m = [0] * (N * 4)
    tree_t = [0] * (N * 4)
    tree_l = [0] * (N * 4)
    tree_r = [0] * (N * 4)

    def init(left=1, right=N, idx=1):
        if left == right:
            tree_t[idx] = tree_r[idx] = tree_l[idx] = G[left]

        else:
            mid = (left + right) // 2
            left_l, left_t, left_r = init(left, mid, idx * 2)
            right_l, right_t, right_r = init(mid + 1, right, idx * 2 + 1)

            tree_t[idx] = left_t + right_t
            tree_l[idx] = max(left_l, left_t, left_t + right_l, left_t + right_t, 0)
            tree_r[idx] = max(right_r, right_t, right_t + left_r, left_t + right_t, 0)

        return tree_l[idx], tree_t[idx], tree_r[idx]

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
            return get_item(cls, left, right, start, mid, idx * 2) + \
                   get_item(cls, left, right, mid + 1, end, idx * 2 + 1)

    init()
    print(tree_t)
    print(tree_r)
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())

        r = get_item("right", x1, y1)
        m = get_item("total", y1 + 1, x2 - 1) if y1 + 1 <= x2 - 1 else 0
        l = get_item("left", x2, y2)
        print(r, m, l)


def solution2():
    N = int(input())
    G = list(map(int, input().split()))
    M = int(input())
    result = []
    for _ in range(M):
        res = -inf
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(x1-1, y1):
            for j in range(x2-1, y2):
                res = max(res, sum(G[i:j+1]))
        result.append(res)
    return result

if __name__ == '__main__':
    result = solution()
    for i in result:
        print(i)
