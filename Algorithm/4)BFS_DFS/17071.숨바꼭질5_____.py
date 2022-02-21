from collections import deque

N, M = map(int, input().split())

Nq = deque()

Nq.append([0, N])  # time, coordinate.

leng = 500001
INF = float("inf")
odd = [INF] * leng
even = [INF] * leng

even[N] = 0
while Nq:  # 언니
    time, X = Nq.popleft()

    for xi in [X+1, X-1, X*2]:
        if 0 <= xi < leng:
            if (time + 1)% 2 == 0 and even[xi] > time + 1 :  # even
                even[xi] = time + 1
                Nq.append([time+1, xi])

            elif odd[xi] > time + 1:  # odd
                odd[xi] = time + 1
                Nq.append([time+1, xi])
def sis():
    graph = [INF] * leng
    graph[M] = 0
    Nq.append([0, M])  # time, coordinate.
    while Nq: #  동생
        time, X = Nq.popleft()
        if odd[X] <= time and (odd[X] - time) // 2 == 0:
            return time
        if even[X] <= time and (even[X] - time) // 2 == 0:
            return time

        time += 1

        for Xi in [X + time]:
            if 0 <= Xi < leng and graph[Xi] > time:
                Nq.append([time, Xi])
                graph[Xi] = time
    return -1

print(sis())