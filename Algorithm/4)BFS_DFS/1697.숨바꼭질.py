from collections import deque

dq = deque()

N, K = map(int, input().split())

check = [float("inf")] * 100001
dq.append(N)
check[N] = 0

while check[K] == float("inf"):
    N = dq.popleft()

    for n2 in [N * 2, N - 1, N + 1]:

        if n2 >= 0 and n2 <= 100000 and check[n2] == float("inf"):
            check[n2] = check[N] + 1
            dq.append(n2)

print(check[K])
