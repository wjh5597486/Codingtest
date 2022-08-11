import sys
inf = float("inf")

def solution():

    def tree_update(start, end, node, idx, num):
        if idx < start or end < idx:
            return

        tree[node] += num

        if start == end:
            return

        mid = (start + end) // 2
        tree_update(start, mid, node*2, idx, num)
        tree_update(mid+1, end, node*2 + 1, idx, num)

    def tree_find(start, end, node, left, right):
        if right < start or end < left:
            return 0

        if left <= start and end <= right:
            value.append(tree[node])
            return

        mid = (start + end) // 2
        tree_find(start, mid, node*2, left, right)
        tree_find(mid+1, end, node*2 + 1, left, right)


    N, M = map(int, input().split())

    tree = [0] * (N*4)
    graph = [0] * (N+1)


    for j in range(M):
        k, a, b = map(int, sys.stdin.readline().split())

        if k == 0:
            value = [0]
            a, b = min(a, b), max(a, b)
            tree_find(1, N, 1, a, b)
            print(sum(value))
        else:
            num = b - graph[a]
            tree_update(1, N, 1, a, num)
            graph[a] = b

if __name__ == '__main__':
    solution()