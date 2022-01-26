from collections import deque

dq = deque()
dq2 = deque()
N, K = map(int, input().split())

check = [float("inf")] * 100001
# initialization
check[N] = 0
dq.append([N, 0])


while check[K] == float("inf"):
    # route, number
    route, number = dq.popleft()

    for n2 in [route * 2, route - 1, route + 1]:
        # out of range, Redundancy
        if 0 <= n2 <= 100000 and check[n2] == float("inf"):
            check[n2] = route
            dq.append([n2, number + 1])


# recall
route, number = dq.pop()
routes = [K]

while route != N:
    routes.append(check[route])
    route = check[route]
# result
print(number)
print(*routes[::-1])