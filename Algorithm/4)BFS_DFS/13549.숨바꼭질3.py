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
            if n2 == N * 2:
                i = 0
            else:
                i = 1
            check[n2] = check[N] + i
            dq.append(n2)

print(check[K])
