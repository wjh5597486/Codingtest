from collections import deque

N, K = map(int, input().split())
dq = deque()

check = [float("inf")] * 100001
dq.append(N)

check[N] = 0

if N == K:
    i = 1
else:
    i = 0

while dq:
    N = dq.popleft()
    for n2 in [N - 1, N * 2, N + 1]:
        if n2 < 0 or n2 > 100000:
            continue

        if check[n2] <= check[N]:
            continue

        dq.append(n2)
        check[n2] = check[N] + 1

        if n2 == K:
            i += 1
            continue

print(check[K])
print(i)