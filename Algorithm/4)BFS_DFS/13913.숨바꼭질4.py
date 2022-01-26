from collections import deque

dq = deque()
dq2 = deque()
N, K = map(int, input().split())

check = [float("inf")] * 100001
dq.append([N])
check[N] = 0

while check[K] == float("inf"):
    N = dq.popleft()

    for n2 in [N[-1] * 2, N[-1] - 1, N[-1] + 1]:

        if 0 <= n2 <= 100000 and check[n2] == float("inf"):
            check[n2] = N + [n2]
            dq.append(N + [n2])
        if n2 == K:
            print(len(check[K])-1)
            print(*check[K])

if N == K:
    print(0)
    print(K)