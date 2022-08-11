import sys
inf = float("inf")

def solution():

    def tree_update(start, end, node, idx, num):
        if idx < start or end < idx:
            return

        tree[node][0] = min(tree[node][0], num)
        tree[node][1] = max(tree[node][1], num)

        if start == end:
            return

        mid = (start + end) // 2
        tree_update(start, mid, node*2, idx, num)
        tree_update(mid+1, end, node*2 + 1, idx, num)

    def tree_find(start, end, node, left, right): # [1, N, 1, 5, 8]
        if right < start or end < left:
            return 0

        if left <= start and end <= right:
            value.append(tree[node][0])
            value.append(tree[node][1])
            return

        mid = (start + end) // 2
        tree_find(start, mid, node*2, left, right)
        tree_find(mid+1, end, node*2 + 1, left, right)




    N, M = map(int, input().split())
    tree = [[inf, 0] for i in range(N*4)]

    for i in range(1,N +1):
        num = int(sys.stdin.readline())
        tree_update(1, N, 1, i, num)

    for j in range(M):
        a, b = map(int, sys.stdin.readline().split())
        value = []
        tree_find(1, N, 1, a, b)
        print(min(value), max(value))


if __name__ == '__main__':
    solution()