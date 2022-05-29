import sys
def solution():
    N = int(input())
    G = []
    for i in range(N):
        G.append(list(map(int, sys.stdin.readline().split())))
    MAX = [0] * 3
    MIN = [0] * 3
    MAX_save = [0] * 3
    MIN_save = [0] * 3

    for r in range(N):
        g = G[r][0]
        MAX_save[0] = max(g+MAX[0], g+MAX[1])
        MIN_save[0] = min(g+MIN[0], g+MIN[1])
        g = G[r][1]
        MAX_save[1] = max(g+MAX[0], g+MAX[1], g+MAX[2])
        MIN_save[1] = min(g+MIN[0], g+MIN[1], g+MIN[2])
        g = G[r][2]
        MAX_save[2] = max(g+MAX[1], g+MAX[2])
        MIN_save[2] = min(g+MIN[1], g+MIN[2])

        MAX = MAX_save.copy()
        MIN = MIN_save.copy()


    print(max(MAX), min(MIN))



if __name__ == "__main__":
    solution()


