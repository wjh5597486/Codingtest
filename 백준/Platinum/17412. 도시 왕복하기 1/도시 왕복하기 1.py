from collections import deque
import sys
sys.setrecursionlimit(200000)
def solution():
    max_p = 401
    N, P = map(int, input().split())
    capacity = [[0]*max_p for i in range(max_p)]

    for i in range(P):
        a, b = map(int, input().split())
        capacity[a][b] = 1

    flows = [[0] * max_p for i in range(max_p)]

    def bfs(start, end):
        dq = deque()
        dq.append(start)
        root[start] = start

        while dq:
            x = dq.popleft()

            if x == end:
                return True

            for i in range(1, max_p):
                if root[i] != -1:
                    continue
                if capacity[x][i] - flows[x][i] > 0:
                    dq.append(i)
                    root[i] = x
        return False

    def turn_on(start, end):
        posterior = end
        while posterior != start:
            prior = root[posterior]
            flows[prior][posterior] += 1
            flows[posterior][prior] -= 1
            posterior = prior

    cnt = 0
    while True:
        root = [-1] * max_p

        if bfs(1,2):
            turn_on(1,2)
            cnt += 1
        else:
            break

    print(cnt)


if __name__ == '__main__':
    solution()
