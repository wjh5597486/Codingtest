import sys
DD = 1_000_000_007
def solution():

    def fill_graph(idx, start, end):
        if start == end:
            tree[idx] = G[start]
            return tree[idx]

        mid = (start + end) // 2
        tree[idx] = fill_graph(idx * 2, start, mid) * fill_graph(idx * 2 + 1, mid + 1, end) % DD

        return tree[idx]


    def sum_graph(idx, start, end, left, right):

        if left > end or right < start:
            return 1

        if left <= start and end <= right:
            return tree[idx]

        mid = (start + end) // 2
        return sum_graph(idx * 2, start, mid, left, right) * sum_graph(idx * 2 + 1, mid + 1, end, left, right)


    def modify_graph(start, end, idx, node, value):

        if node < start or node > end:
            return

        if start == end:
            tree[idx] = value
            return

        mid = (start + end) // 2
        modify_graph(start, mid, idx*2, node, value)
        modify_graph(mid+1, end, idx*2 + 1, node, value)

        tree[idx] = tree[idx*2] * tree[idx*2 + 1] % DD

    N, M, K = map(int, input().split())

    G = [0]
    tree = [0] * (N*4)

    for _ in range(N):
        G.append(int(input()))

    fill_graph(1, 1, N)

    for _ in range(M + K):
        a, b, c = map(int, input().split())

        if a == 1:
            modify_graph(1, N, 1, b, c)
            G[b] = c

        elif a == 2:
            print(sum_graph(1, 1, N, b, c) % DD)


if __name__ == '__main__':
    solution()