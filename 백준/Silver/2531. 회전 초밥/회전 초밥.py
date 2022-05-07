import sys


def solution():
    N, d, k, c = map(int, input().split())
    G = []
    for i in range(N):
        G.append(int(sys.stdin.readline()))
    G = G + G
    l = -1
    r = k-1
    LIST = [0] * 3010
    number = 0
    for i in [c, *G[:r+1]]:
        if LIST[i] == 0:
            number += 1
        LIST[i] += 1
    result = number

    while True:
        l +=1
        r +=1
        if r >= len(G):
            break

        num = G[l]
        LIST[num] -= 1
        if LIST[num] == 0:
            number -= 1

        num = G[r]
        LIST[num] += 1
        if LIST[num] == 1:
            number += 1

        result = max(result, number)
    print(result)


if __name__ == '__main__':
    solution()
