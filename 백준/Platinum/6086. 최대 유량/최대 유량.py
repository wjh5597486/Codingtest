from collections import deque
def solution():
    capacity = [[0]*150 for i in range(150)]
    for i in range(int(input())):
        a, b, c = input().split()
        a, b = ord(a), ord(b)
        capacity[a][b] += int(c)
        capacity[b][a] += int(c)

    flows = [[0] * 150 for i in range(150)]

    def bfs(start, end):
        dq = deque()
        dq.append(start)
        root[start] = start

        while dq:
            x = dq.pop()

            if x == end:
                return True

            for i in range(150):
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
            posterior = prior

    cnt = 0
    while True:
        root = [-1] * 150
        if bfs(ord('A'), ord('Z')):
            cnt += 1
            turn_on(ord('A'), ord('Z'))
        else:
            break
    print(cnt)


if __name__ == '__main__':
    solution()
