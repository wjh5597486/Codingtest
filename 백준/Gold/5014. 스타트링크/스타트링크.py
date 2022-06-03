from collections import deque

def solution():
    F, S, goal, U, D = map(int, input().split())
    G = [0] * (F+1)
    G[S] = 0
    if S == goal:
        print(0)
    else:

        dq = deque()
        dq.append([S, 0])
        while dq:
            x, n = dq.popleft()
            for x2 in [x+U, x-D]:
                if 1 <= x2 <=F:
                    if G[x2] == 0:
                        dq.append([x2, n+1])
                        G[x2] = n+1

        if G[goal] == 0:
            print("use the stairs")
        else:
            print(G[goal])




if __name__ == "__main__":
    solution()
